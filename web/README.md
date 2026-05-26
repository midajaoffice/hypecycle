# HypeCycle Dashboard

Interne Visualisierung — liest direkt aus `täglich/portfolio-state.md` und `decision-log-recent.md`.

## Starten

```bash
cd "/Users/dreamwalker/Desktop/Buisness/HyperCycle/google-drive/HypeCycle"
chmod +x web/start.sh
./web/start.sh
```

Browser: **http://localhost:8765/web/**

Nach jedem ChatGPT-Sync in Google Drive: Seite neu laden oder **Aktualisieren**.

## Hinweis

`file://` funktioniert nicht (Browser blockiert `fetch`). Immer über den lokalen Server starten.

## Optional

Anderen Port: `PORT=3000 ./web/start.sh`
