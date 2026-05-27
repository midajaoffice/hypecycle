# Sync-Regel — Dateien ↔ ChatGPT Project

**Wahrheit:** Git-Repo (`täglich/`, `ideen/`). ChatGPT Project = Arbeitskopie — nach dem Chat lokale Dateien + Project-Dateien anpassen.

**Lebenszyklus:** Bei Kauf/Verkauf/Verwerfen immer [`../chatgpt/operator-protocol.md`](../chatgpt/operator-protocol.md) Abschnitt **Portfolio-Lebenszyklus** beachten (`Ausführung:`, `# REJECTED_IDEA`).

## Einmal ins Project

| Quelle | Dateien |
|---|---|
| `chatgpt/` | `operator-core.md`, `operator-protocol.md` |
| `täglich/` | `portfolio-state.md`, `decision-log-recent.md`, `watchlist.md` |

**Instructions:** [`../chatgpt-instructions.md`](../chatgpt-instructions.md) (Repo = Wahrheit; Mac-Ordner `HyperCycle/chatgpt-instructions.md` spiegeln)

## Nach jedem Briefing

1. `# UPDATED_PORTFOLIO_STATE` → `portfolio-state.md`
2. `# NEW_LOG_ENTRY` → `decision-log.md` **und** `decision-log-recent.md` (inkl. **Ausführung:**)
3. `# UPDATED_WATCHLIST` → `watchlist.md` (bei Status / Verkauf / Verwerfen)
4. `# REJECTED_IDEA` → `ideen/rejected-ideas.md` (nur bei Verwerfen)
5. Project: `portfolio-state` + `decision-log-recent` **ersetzen** (löschen + neu hochladen)

## Operator intern

- GPT liest zuerst **OPERATOR_VIEW** (oben in portfolio-state)
- Pipeline: `operator-protocol.md` Phase 1–5
- Briefing max. ~40 Zeilen; Rechenbudget für Zahlen

## Nicht ins Project

`anleitung/`, `archiv/`, `decision-log.md` (Vollarchiv — nur lokal/Git, nicht ins Project)

## Chats & Memory

- **Neuer Chat** täglich
- Alte Chats nicht weiterführen
- Memory: kein Portfolio-Bestand

## Monatlich

Einträge > 14 Tage aus `decision-log-recent.md` → `archiv/decision-log-archive.md`
