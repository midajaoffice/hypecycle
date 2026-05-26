# Decision Log (vollständig)

**Nicht** die Quelle der Wahrheit — nur Historie. Bestand steht in [`portfolio-state.md`](portfolio-state.md).

**ChatGPT Project** nutzt [`decision-log-recent.md`](decision-log-recent.md) (nur ~14 Tage).

---

## Kurz-Eintrag (Pflicht — max. 15 Zeilen)

Nach jedem Briefing `# NEW_LOG_ENTRY` einfügen in:

1. **diese Datei** (`decision-log.md`)
2. [`decision-log-recent.md`](decision-log-recent.md)

```markdown
## YYYY-MM-DD

**North Star:** Starsumme FEHLT → Ziel 10× FEHLT | Ist FEHLT | Fortschritt FEHLT% | Lücke FEHLT EUR
**DQ:** E | **Fazit:** Keine Aktion | **Kaufen prüfen:** — | **Verkauf prüfen:** —
**Änderungen an portfolio-state:** keine | **Watchlist:** keine
**Gebühren/Steuer heute:** — | **Risiko:** Datenlücken | **Nächster Schritt:** Starsumme eintragen
**Lernnotiz:** Eine Zeile.
```

---

## Regeln

- Kein Vollbriefing, keine Marktessays
- Widerspricht ein alter Eintrag `portfolio-state.md` → **portfolio-state gewinnt**
- `decision-log-recent.md`: Einträge > 14 Tage → nach [`../archiv/decision-log-archive.md`](../archiv/decision-log-archive.md) verschieben
- Diese Datei: optional ältere Einträge monatlich archivieren

---

## 2026-05-27 (Erstkauf)

**North Star:** 500→5000 EUR | Ist 498 EUR | Fortschritt 10,0 % | Lücke 4.502 EUR
**DQ:** B | **Fazit:** Erstkauf RKLB + UEC | **Kaufen prüfen:** — | **Verkauf prüfen:** —
**Änderungen:** RKLB 125 EUR, UEC 100 EUR; Cash 273 EUR; 2× Gebühr 1 EUR | **Watchlist:** RKLB/UEC → Position
**Gebühren/Steuer:** 2 EUR Orders; PV 498 nach Gebühren | **Risiko:** 45 % investiert, 55 % Cash
**Nächster Schritt:** Broker-Fills in §4; Kurse aktualisieren; ASTS/RCAT beobachten
**Lernnotiz:** Gates eingehalten (125/100 €); Reserve bewusst groß gelassen.

---

## 2026-05-26 (Erst-Zyklus)

**North Star:** 500→5000 EUR | Ist 500 EUR | Fortschritt 10,0 % | Lücke 4.500 EUR
**DQ:** C | **Fazit:** Watchlist erstellt, keine Ausführung | **Kaufen prüfen:** RKLB 125 €, UEC 100 € | **Verkauf prüfen:** —
**Änderungen:** OPERATOR_VIEW watchlist_top=RKLB,UEC; Positionen weiter keine | **Watchlist:** 8 Kandidaten
**Gebühren/Steuer:** RKLB RT 2,63 €/BE 2,10 %; UEC RT 2,50 €/BE 2,50 %; DE-Modell 26,375 % über 1.000 € Freistellung
**Risiko:** 10×-Ziel extrem ambitioniert; DQ C wegen Broker/Fractionals/FX offen
**Nächster Schritt:** Mission Control prüft Broker-Ausführung, Fractionals, Limitkurs, danach §4 nur bei echter Order ergänzen
**Lernnotiz:** Bei 500 € Start keine Kleinsttickets; Gebühren erzwingen hohe Conviction.
