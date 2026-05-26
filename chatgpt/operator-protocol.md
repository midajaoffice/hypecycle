# Operator Protocol — 5-Phasen-Pipeline

**Pflicht:** Jeden Chat in dieser Reihenfolge. Phasen 1–4 **intern** — nicht als Prosa im Chat ausgeben.

Details: [`operator-core.md`](operator-core.md) · Lese-Header: `portfolio-state.md` → **OPERATOR_VIEW**

---

## Phase 1 — READ

1. Nur **`OPERATOR_VIEW`** in `portfolio-state.md` lesen
2. Bei Lücken gezielt: §4 Positionen, §5 Watchlist, §0 North Star
3. `decision-log-recent.md` — letzte Entscheidungen, **nicht** Bestand
4. **Nicht** ChatGPT Memory für Zahlen

---

## Phase 2 — VALIDATE

- Datenqualität **A–E** aus portfolio-state
- **D oder E:** keine starken Kauf/Verkauf-Calls → ACT = `daten_pruefen` / `keine_aktion`
- Fehlende Felder: max. **3** Stichwörter für Briefing-Zeile `VAL`

---

## Phase 3 — RESEARCH

- Web Search für Kurse, News, Katalysatoren
- Jede Aussage intern: **Fakt** | **Annahme** | **Spekulation**
- Unverifiziert = **NICHT VERIFIZIERT** — nichts erfinden
- **Links** nur in Watchlist/§-Text der Blöcke, **nicht** im Briefing

---

## Phase 4 — SCORE

Pro Kandidat (Watchlist oder Position), Score **1–10** je Kriterium:

| Kriterium | Gewichtung |
|---|---|
| Katalysator-Stärke | hoch |
| Timing | hoch |
| Hype-Potenzial | mittel |
| Risiko | hoch (niedriger Score = riskanter) |
| Gebühren-Impact (bei 500 €) | hoch |
| Portfolio-Fit / North Star | mittel |

**Gesamt** ≈ Durchschnitt oder begründeter Mix → Status: Beobachten | Kaufen prüfen | Verkauf prüfen | Daten prüfen | Position

### Positionsgrößen (Starsumme 500 €)

| Typ | % | EUR (Richtwert) |
|---|---|---|
| Hype-Idee | 5–10 % | 25–50 |
| Normale Spekulation | 10–20 % | 50–100 |
| Maximum Einzelposition | 30 % | 150 |
| Cash-Reserve | Pflicht | nicht All-in |

### Trade-Gate (Pflicht bei „Kaufen prüfen“)

```
round_trip_eur ≈ 2 × FEE_ORDER + 2 × (POSITION_EUR × SLIPPAGE_PCT)
break_even_pct ≈ round_trip_eur / POSITION_EUR × 100
```

Defaults: FEE_ORDER = 1 €, SLIPPAGE_PCT = 0,25 %

**Steuer (Modell DE):** Gewinn über Freistellung (1.000 €) × 26,375 % — grob, keine Beratung.

**Gate:** break_even + Noise > Edge → Status **Daten prüfen** / **Beobachten** (nicht K1/K2).

---

## Phase 5 — EMIT

### A) Briefing (Teil 1 der Antwort)

Überschrift: `### Briefing — YYYY-MM-DD`

**Max. 12 nummerierte Zeilen**, Schema siehe `chatgpt-instructions.md` (Project Instructions).

**Beispiel Erst-Zyklus (Cash, 2× Kaufen prüfen):**

```text
### Briefing — 2026-05-26
1. READ — cash=500 invest=0 pv=500 pos=keine dq=C
2. NS — 500→5000|10.0%|lücke=4500|tag=1/365
3. VAL — dq=C|broker,fractionals,fx
4. ACT — keine_ausfuehrung|watchlist_8
5. K1 — RKLB|7.2|eur=125|rt=2.63|be=2.10%|gate=kein_momentum_chase
6. K2 — UEC|6.9|eur=100|rt=2.50|be=2.50%|gate=uran_beta
8. RAD — ASTS:beobachten,RCAT:beobachten,KTOS:beobachten,SMCI:beobachten,VRT:daten_prüfen,CRSR:beobachten
9. RISK — 10x_ambitioniert;gebuehren_kleine_tickets
10. NEXT — broker_us_fractionals_rklb_limit
```

**Beispiel mit Positionen:**

```text
### Briefing — 2026-05-27
1. READ — cash=273 invest=225 pv=498 pos=RKLB,UEC dq=B
2. NS — 500→5000|10.0%|lücke=4502|tag=2/365
3. VAL — dq=B|broker_fill,fx_kurse
4. ACT — halten|kein_neukauf
7. POS — RKLB/Rocket Lab:125@135.76 pnl=0%,UEC/Uranium Energy:100@13.02 pnl=0%
8. RAD — ASTS:beobachten,RCAT:beobachten
9. RISK — bewertung_rklb;uran_vol
10. NEXT — kurse_verifizieren_broker_fill
```

(Zeile 7 `POS` ersetzt K1/K2 wenn keine neuen Kauf-/Verkauf-Prüfungen.)

### B) Sync-Blöcke (Teil 2 — für Mission Control)

| Reihenfolge | Block | Inhalt |
|---:|---|---|
| 1 | `# UPDATED_PORTFOLIO_STATE` | **Vollständige** Datei; OPERATOR_VIEW = Briefing-Zahlen |
| 2 | `# UPDATED_WATCHLIST` | bei Watchlist-/Status-Änderung |
| 3 | `# NEW_LOG_ENTRY` | max. 15 Zeilen |

**Zwischen Blöcken:** kein Kommentar, keine Wiederholung des Briefings.

### C) NEW_LOG_ENTRY Vorlage

```markdown
## YYYY-MM-DD
**North Star:** 500→5000|Ist …|Fortschritt …%|Lücke … EUR
**DQ:** … | **Fazit:** … | **Kaufen prüfen:** … | **Verkauf prüfen:** …
**Änderungen:** … | **Watchlist:** …
**Gebühren/Steuer:** … | **Risiko:** … | **Nächster Schritt:** …
**Lernnotiz:** …
```

### D) Optional

`# OPERATOR_SNAPSHOT` — HCSP-lite, nicht für Google ([`hcsp-lite.md`](hcsp-lite.md))
