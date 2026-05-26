# Sync-Regel — Google ↔ ChatGPT

## Einmal ins Project

| Quelle | Dateien |
|---|---|
| `chatgpt/` | `operator-core.md`, `operator-protocol.md` |
| `täglich/` | `portfolio-state.md`, `decision-log-recent.md`, `watchlist.md` |

**Instructions:** Mac `chatgpt-instructions.md`

## Nach jedem Briefing

1. `# UPDATED_PORTFOLIO_STATE` → Google `portfolio-state.md`
2. `# NEW_LOG_ENTRY` → Google `decision-log.md` **und** `decision-log-recent.md`
3. Project: `portfolio-state` + `decision-log-recent` **ersetzen** (löschen + neu hochladen)

## Operator intern

- GPT liest zuerst **OPERATOR_VIEW** (oben in portfolio-state)
- Pipeline: `operator-protocol.md` Phase 1–5
- Briefing max. ~40 Zeilen; Rechenbudget für Zahlen

## Nicht ins Project

`anleitung/`, `archiv/`, `decision-log.md` (Vollarchiv nur Google)

## Chats & Memory

- **Neuer Chat** täglich
- Alte Chats nicht weiterführen
- Memory: kein Portfolio-Bestand

## Monatlich

Einträge > 14 Tage aus `decision-log-recent.md` → `archiv/decision-log-archive.md`
