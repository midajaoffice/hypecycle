# HCSP-Lite (optional, nur im Chat)

**Nicht** in Google speichern. Optional am Ende eines Briefings als `# OPERATOR_SNAPSHOT`.

---

## Format

```
@HCSP 1.0
@TYPE SNAPSHOT
@DATE YYYY-MM-DD

@@VIEW
north_star: 500→5000|fortschritt:10%|luecke:4500
kapital: cash=500|pv=500|dq=C
positionen: keine
watchlist_top: TICK1,TICK2
```

---

## Regeln

- Spiegel von `OPERATOR_VIEW` + Änderungen des Tages
- `MISS` = fehlend, `NV` = nicht verifiziert
- Markdown (`portfolio-state.md`) bleibt Wahrheit
