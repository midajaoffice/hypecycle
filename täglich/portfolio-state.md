# Portfolio State

**Letztes Update:** 2026-05-27
**Datenqualität:** B
**Modus:** Modellportfolio / Research-Unterstützung

> **Einzige Quelle der Wahrheit** für Bestand, Cash und Kurse. ChatGPT Memory zählt nicht.

---

## OPERATOR_VIEW

> Operator: **zuerst nur diesen Block lesen.** Bei jedem Update vollständig aktualisieren.

```
north_star: 500→5000|EUR|fortschritt:10.0%|luecke:4502|tag:3/365|ziel_datum:2027-05-25
kapital: cash=273|investiert=225|pv=498|dq=B
modus: maintenance
positionen: RKLB,UEC
positionen_detail: RKLB pnl=0% trigger_kurs=ok trigger_news=watch next=neutron_Q2|UEC pnl=0% trigger_kurs=offen trigger_news=uran next=burke_hollow
watchlist_top: ASTS,RCAT
letzte_entscheidung: halten|keine_ausfuehrung_kein_neukauf|2026-05-27
gebuehren_modell: 1EUR/order|0.25pct_slippage|steuer_modell:26.375pct_DE
```

**Felder:** `modus` = maintenance | thesis_scan | action (MC setzt vor Chat, siehe `anleitung/mc-datenritual.md`). `positionen_detail` — MC: pnl, next; Operator: trigger_kurs, trigger_news.

---

## 0. North Star

| Feld | Wert |
|---|---|
| **Starsumme (Startkapital)** | **500 EUR** |
| **Startdatum North Star** | **2026-05-25** |
| **Zielhorizont** | bis **2027-05-25** |
| **Ziel-Multiple** | **10×** ohne Hebel |
| **Zielwert (TARGET_VALUE_EUR)** | **5.000 EUR** |
| **Aktueller Fortschritt %** | **10,0 %** (498 ÷ 5.000) |
| **Lücke bis Ziel (EUR)** | **4.502 EUR** |
| **Erforderliche Gesamtrendite** | +900 % in 12 Monaten, Orientierung |

### Kosten- & Steuer-Modell

| Feld | Wert |
|---|---|
| Broker-Modell | EU-Online-Broker, zu bestätigen |
| Gebühr pro Order | 1,00 EUR |
| Slippage-Annahme pro Seite | 0,25 % |
| Steuersatz Modell DE | 26,375 % |
| Freistellungsauftrag | 1.000 EUR/Jahr |
| Kirchensteuer | nein |

---

## 1. Mission

Spekulatives Modellportfolio von 500 EUR auf 5.000 EUR innerhalb von 12 Monaten bringen — ohne Hebel, nur Aktien/ETFs/Rohstoff-ETPs über regulierte Börsen. North Star dient der Priorisierung, nicht als Renditeversprechen.

**Erlaubt:** Aktien, ETFs, Rohstoff-ETPs/ETCs — Xetra, Frankfurt, NYSE, NASDAQ, Euronext  
**Ausgeschlossen:** Krypto, Forex, CFDs, Optionen, Hebelprodukte, illiquide/unregulierte Märkte.

---

## 2. Kapital

| Feld | Wert |
|---|---:|
| Startkapital | 500 |
| Aktueller geschätzter Portfoliowert | 498 |
| Verfügbares Cash | 273 |
| Investiertes Kapital | 225 |
| Nicht verifizierte Werte | Kurse/FX nach Erstkauf (Research-Kurs) |

---

## 3. Portfolio-Regeln

- Keine echten Trades ohne menschliche Bestätigung.
- Max. **4** gleichzeitige Positionen in §4.
- Min. **20 %** Cash-Reserve am PV (Ausnahme nur mit Begründung im Decision Log).
- Keine Position über 30 % des Modellportfolios.
- Hype-Ideen maximal 5–10 %, normale Spekulationen 10–20 %.
- Keine Nachkäufe aus Hoffnung.
- Jede Position braucht These, Katalysator und **Exit-Kriterium** (Stop/These in §4).
- **Gewinnmitnahme:** optional prüfen ab ca. **+30 %** pnl oder wenn Position > 30 % PV — Verkauf nur nach Mission-Control-Bestätigung.
- Keine Kaufprüfung ohne aktuelle Kursprüfung.
- Watchlist-Radar: **5–8** Namen (Beobachten/Kaufen prüfen); Verworfenes → `ideen/rejected-ideas.md`.
- Lebenszyklus-Details: `chatgpt/operator-protocol.md` → **Portfolio-Lebenszyklus**.

---

## 4. Aktuelle Positionen

| Asset | Ticker | Markt | Kaufdatum | Kaufkurs | Aktueller Kurs | Positionsgröße | Positionswert | These | Katalysator | Trigger-Typ | Nächstes Event | Stop/Exit | Status | DQ |
|---|---|---|---|---:|---:|---:|---:|---|---|---|---|---|---|---|
| Rocket Lab | RKLB | NASDAQ | 2026-05-26 | 135,76 USD | 135,76 USD | 125 EUR | 125 | Space-Defense-Wachstum, Launch-Backlog | Q1 Rekorde, Neutron, Space Force | Beides | Neutron / Q2 | Verkauf prüfen bei -15 % oder These bricht (Neutron-Verzug) | Offen | B |
| Uranium Energy Corp | UEC | NYSE American | 2026-05-26 | 13,02 USD | 13,02 USD | 100 EUR | 100 | US-Uran-Produktion, Fuel-Security | Burke Hollow, Uranpreis | Beides | Burke Hollow / Uranpreis | Verkauf prüfen bei -15 % oder Uranpreis-/Ramp-Bruch | Offen | B |

---

## 5. Watchlist-Zusammenfassung

| Asset | Ticker | Markt | Thema | Katalysator | Risiko | Story | Setup | Score | Status | Nächster Prüfpunkt |
|---|---|---|---|---|---|---:|---:|---:|---|---|
| Rocket Lab | RKLB | NASDAQ | Space/Defense | Q1 Rekorde, Backlog, Space Force, Neutron | Bewertung/Momentum | 7.2 | 7.2 | 7.2 | Position | Stop/These monatlich |
| Uranium Energy Corp | UEC | NYSE American | Uran/Rohstoffe | Burke Hollow, Uranpreis, US Fuel-Security | Uranpreis/Ramp-up | 6.9 | 6.9 | 6.9 | Position | Uranpreis + Produktionsnews |
| AST SpaceMobile | ASTS | NASDAQ | Space/Satcom | 2026 Revenue Guidance, FCC, Satelliten-Ramp | Launch-/Capex-Risiko | 6.6 | 6.6 | 6.6 | Beobachten | BlueBird-Launch-Kadenz prüfen |
| Red Cat | RCAT | NASDAQ | Defense/Drohnen | Army/SRR, Q1 Umsatzsprung | Earnings-Miss, Margen | 6.5 | 6.5 | 6.5 | Beobachten | Q2 Margen/Army-Deliveries |
| Kratos Defense | KTOS | NASDAQ | Defense/Unmanned | Q1 Wachstum, Guidance erhöht | hohe Bewertung | 6.4 | 6.4 | 6.4 | Beobachten | neue Contracts/Backlog |
| Super Micro | SMCI | NASDAQ | KI-Infrastruktur | AI-Server-Umsatz, FY26 Sales-Guidance | Cashflow/Review/Margen | 6.2 | 6.2 | 6.2 | Beobachten | Cashflow + Export-Control-Review |
| Vertiv | VRT | NYSE | KI-Infrastruktur | Data-center sales +30 %, Guidance erhöht | Preis > 150 € ohne Fractionals, Bewertung | 6.1 | 6.1 | 6.1 | Daten prüfen | Fractional möglich? Bewertung prüfen |
| Corsair Gaming | CRSR | NASDAQ | Gaming/Hardware | Q1 Umsatz +10 %, profitabler Turnaround | Konsum/PC-Zyklus | 5.8 | 5.8 | 5.8 | Beobachten | Gaming-Hardware-Nachfrage |

---

## 6. Offene Prüfpunkte

- Broker-Fills bestätigen: exakte Stückzahl, FX-Kurs, Gebühren in §4 nachziehen.
- RKLB/UEC: Aktuelle Kurse vs. Kaufkurs; P&L in EUR schätzen.
- Uranpreis und Burke-Hollow-News für UEC laufend beobachten → danach Operator-Modus `thesis_scan`.
- Cash-Reserve 273 EUR (~55 %) bewusst halten — kein Nachkauf ohne stärkere These.
- **Ohne MC-Kursupdate:** Operator bleibt in `modus: maintenance` (kein erfundenes pnl). Ritual: [`anleitung/mc-datenritual.md`](../anleitung/mc-datenritual.md).

---

## 7. Bekannte Unsicherheiten

- Erstkauf RKLB/UEC eingetragen; Kaufkurse = Research-Stand bis Broker-Fill bestätigt.
- DQ **B**: Positionen dokumentiert, Broker-Fill/FX noch verfeinern.
- Aktuelle Kurse = Kaufkurs (kein Intraday-Update); PV 498 EUR inkl. 2 € Ordergebühren.
- 10×-North-Star ist extrem ambitioniert und keine Garantie.
- Steuer/Broker nur Modellannahmen.

---

## 8. Letzte Änderungen

- 2026-05-27: Keine Ausführung; keine Cash-/Positions-/Statusänderung; OPERATOR_VIEW auf Tag 3/365 aktualisiert.
- 2026-05-26: RKLB (125 EUR) und UEC (100 EUR) gekauft; Cash 273 EUR; 2× 1 EUR Gebühr.
- 2026-05-25: Ursprungsportfolio; Watchlist mit 8 Kandidaten; RKLB/UEC „Kaufen prüfen“, keine Positionen.
