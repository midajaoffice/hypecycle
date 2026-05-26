#!/usr/bin/env python3
"""Display HypeCycle portfolio from täglich/portfolio-state.md (stdlib only)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "täglich" / "portfolio-state.md"


def load_state() -> str:
    if not STATE_FILE.is_file():
        print(f"Error: not found: {STATE_FILE}", file=sys.stderr)
        sys.exit(1)
    return STATE_FILE.read_text(encoding="utf-8")


def meta_value(text: str, label: str) -> str:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*([^\n*]+)", text)
    return m.group(1).strip() if m else "—"


def parse_operator_view(text: str) -> dict[str, str]:
    m = re.search(r"## OPERATOR_VIEW.*?```\n(.*?)```", text, re.DOTALL)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).strip().splitlines():
        if ":" not in line:
            continue
        key, rest = line.split(":", 1)
        out[key.strip()] = rest.strip()
    return out


def parse_kv_line(line: str) -> dict[str, str]:
    """Parse 'cash=500|fortschritt:10.0%' style pipe-separated segments."""
    parts: dict[str, str] = {}
    for chunk in line.split("|"):
        for sep in ("=", ":"):
            if sep in chunk:
                k, v = chunk.split(sep, 1)
                parts[k.strip()] = v.strip()
                break
    return parts


def section(text: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}.*?\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1) if m else ""


def parse_markdown_table(block: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or all(set(c) <= {"-", ":"} for c in cells):
            continue
        rows.append(cells)
    return rows


def fmt_eur(value: str) -> str:
    try:
        n = float(value.replace(",", "."))
        return f"{n:,.2f} EUR".replace(",", "X").replace(".", ",").replace("X", ".")
    except ValueError:
        return value


def print_header(title: str) -> None:
    width = 72
    print()
    print(title)
    print("-" * width)


def print_kv(pairs: list[tuple[str, str]], indent: int = 2) -> None:
    pad = max((len(k) for k, _ in pairs), default=0)
    for key, val in pairs:
        print(f"{' ' * indent}{key:<{pad}}  {val}")


def main() -> None:
    text = load_state()
    ov = parse_operator_view(text)

    print("=" * 72)
    print("  HypeCycle — Portfolio")
    print("=" * 72)
    print(f"  Source: {STATE_FILE.relative_to(ROOT)}")
    print(f"  Updated: {meta_value(text, 'Letztes Update')}")
    print(f"  DQ: {meta_value(text, 'Datenqualität')}  |  Mode: {meta_value(text, 'Modus')}")

    # North Star from OPERATOR_VIEW
    print_header("North Star")
    ns_line = ov.get("north_star", "")
    ns = parse_kv_line(ns_line)
    goal = re.search(r"(\d+)→(\d+)", ns_line)
    start_eur, target_eur = goal.groups() if goal else ("?", "?")
    print_kv(
        [
            ("Goal", f"{start_eur} → {target_eur} EUR (by {ns.get('ziel_datum', '—')})"),
            ("Progress", ns.get("fortschritt", "—")),
            ("Gap", f"{ns.get('luecke', '—')} EUR"),
            ("Day", ns.get("tag", "—")),
        ]
    )

    # Capital
    print_header("Capital")
    kap = parse_kv_line(ov.get("kapital", ""))
    print_kv(
        [
            ("Cash", fmt_eur(kap.get("cash", "—"))),
            ("Invested", fmt_eur(kap.get("investiert", "—"))),
            ("Portfolio value", fmt_eur(kap.get("pv", "—"))),
            ("Data quality", kap.get("dq", meta_value(text, "Datenqualität"))),
        ]
    )

    cap_rows = parse_markdown_table(section(text, "2. Kapital"))
    if cap_rows:
        print()
        for label, val in cap_rows:
            print(f"    {label:<35} {val}")

    # Last decision
    print_header("Last decision")
    ents = ov.get("letzte_entscheidung", "—")
    parts = ents.split("|")
    if len(parts) >= 2:
        print_kv([("Action", parts[0]), ("Detail", parts[1]), ("Date", parts[2] if len(parts) > 2 else "—")])
    else:
        print(f"  {ents}")
    print(f"  Watchlist top: {ov.get('watchlist_top', '—')}")

    # Positions
    print_header("Positions")
    pos_rows = parse_markdown_table(section(text, "4. Aktuelle Positionen"))
    if not pos_rows:
        print("  (no table found)")
    else:
        headers = pos_rows[0]
        data = pos_rows[1:]
        if len(data) == 1 and data[0][0].lower() in ("keine", "fehlt"):
            print("  No open positions — 100% cash.")
        else:
            for row in data:
                ticker = row[1] if len(row) > 1 else "?"
                asset = row[0]
                status = row[10] if len(row) > 10 else ""
                size = row[7] if len(row) > 7 else ""
                print(f"  • {asset} ({ticker})  size={size}  status={status}")

    # Watchlist (compact)
    print_header("Watchlist")
    wl_rows = parse_markdown_table(section(text, "5. Watchlist-Zusammenfassung"))
    if wl_rows and len(wl_rows) > 1:
        for row in wl_rows[1:]:
            if row[0].lower() in ("fehlt", "keine"):
                continue
            asset, ticker, _, theme, _, risk, score, status = (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
            )
            flag = " ★" if "kaufen" in status.lower() else ""
            print(f"  {ticker:<6} {score:>4}  {status:<14}{flag}  {asset} — {theme}")
    else:
        print("  (empty)")

    # Open items
    print_header("Open checks")
    open_sec = section(text, "6. Offene Prüfpunkte")
    for line in open_sec.splitlines():
        line = line.strip()
        if line.startswith("- "):
            print(f"  • {line[2:]}")

    print()
    print("=" * 72)


if __name__ == "__main__":
    main()
