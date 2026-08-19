# Verkehrsmedizin Fragebogen App

Full-Stack-Anwendung für verkehrsmedizinische Anamnese-Fragebögen. Der Fragenkatalog
basiert auf den **Begutachtungsleitlinien zur Kraftfahreignung (BASt, Stand 2022)**
und wird schema-getrieben ausgeliefert: Backend-Template, Patientenformular,
Validierung und PDF arbeiten mit derselben Quelle. Inklusive automatischer
Auswertung der Antworten mit Leitlinien-Konsequenzen (Entscheidungsunterstützung
für die ärztliche Beurteilung),
Epworth Sleepiness Scale (ESS), Admin-Bereich für die Praxis und GDT-Anbindung
an die Praxis-EDV (SAMAS).

## Technologie-Stack

### Backend
- Django 6.0 + Django REST Framework
- PostgreSQL 16 (psycopg 3); lokal optional SQLite (USE_SQLITE=True)
- Automatische BASt-Auswertung (questionnaires/evaluation.py)

### Frontend
- Next.js 16 (App Router) + React 19
- **43 Sprachen**: Länder-Combobox mit SVG-Flaggen (lokal gebündelt, inkl. Kosovo);
  Katalog bleibt deutsch-kanonisch, Sprachdateien übersetzen nur die Patienten-Anzeige,
  PDF/Auswertung bleiben deutsch; RTL für Arabisch/Urdu; Gateway-Frage verkürzt den
  Fragebogen bei Gesunden von 67 auf 45 Fragen
- Tailwind CSS v4 + shadcn/ui (new-york, OKLCH-Theme, Field-Familie)
- react-hook-form (dokumentiertes shadcn-Formular-Muster), sonner-Toasts
- Dark Mode nach shadcn (next-themes): Hell · Dunkel · E-Ink (Praxis-Tablet) · System
- Puppeteer (Design-PDF über die serverseitige Print-Page)

### Integration & Deployment
- GDT-Bridge: Windows-Dienst, der den GDT-Ordner von SAMAS überwacht (`gdt_bridge/`)
- Docker Compose (Produktion auf Synology), `deploy.bat` für Push + Server-Update

## Funktionsweise

1. **Session anlegen** – über den Admin-Bereich (`/admin`-Seite des Frontends) oder
   automatisch durch die GDT-Bridge, wenn SAMAS eine Anforderung in den GDT-Ordner legt.
2. **Patient füllt aus** – Token-Link (`/q/<token>`), 14-Schritte-Formular nach den
   Begutachtungsleitlinien (bedingte Folgefragen, ESS mit Echtzeit-Auswertung,
   Einwilligung mit Datenschutzhinweisen).
3. **Ergebnis** – ESS-Score + Kategorie, PDF-Export (Puppeteer über die
   Print-Seite) inkl. automatischer Leitlinien-Auswertung (kritisch/prüfen/
   Hinweis mit Kapitel-Referenz), Rückmeldung an SAMAS als Ergebnis-GDT.

## Fragenkatalog

Der Katalog liegt in `backend/questionnaires/catalog.py` (14 Abschnitte, ~90 Fragen
mit bedingter Logik) und deckt die anamnese-relevanten Kapitel der
Begutachtungsleitlinien ab: Anfälle/Synkopen, Sehen/Hören, Herz-Kreislauf,
Schlaganfall/Gehirn, Nervensystem, Gleichgewicht/Schwindel, Bewegungsapparat,
Diabetes, innere Organe, Tagesschläfrigkeit/OSAS inkl. ESS, Psyche sowie
Alkohol/Drogen/Medikamente — inklusive der Leitlinien-Zeitfenster (z.B.
anfallsfrei seit, Fremdhilfe-Hypoglykämie in den letzten 12 Monaten) und einer
Steuerfrage für Gruppe 2 (LKW/Bus/Fahrgastbeförderung).

```bash
# Katalog als aktives Template laden (läuft in Docker automatisch beim Start)
python manage.py load_catalog

# i18n: Master aus dem Katalog erzeugen bzw. Sprachdateien prüfen
python manage.py build_i18n_master
python manage.py check_i18n
```

**Mehrsprachigkeit:** `questionnaires/i18n/<code>.json` (42 Sprachen, maschinell
übersetzt und als solche markiert — fachliche Prüfpunkte in
`docs/UEBERSETZUNGS-HINWEISE.md`). Antworten sind sprachunabhängige Werte;
der Sprachwechsel im Formular erhält bereits gegebene Antworten.

Änderungen am Katalog werden mit dem nächsten `load_catalog` wirksam; das Frontend
rendert das Formular vollständig aus dem Template-Schema der Session-API, die
Submit-Validierung, PDF und automatische Auswertung nutzen dasselbe Schema
(eine Quelle, kein Drift).

### Automatische Auswertung

`questionnaires/evaluation.py` prüft die Antworten gegen ein Regelwerk aus den
Begutachtungsleitlinien (z.B. Anfallsfreiheits-Fristen nach Kap. 3.9.6, ESS-Grenzwert
11 nach Kap. 3.11, ICD/Gruppe 2 nach Kap. 3.4.1.4) und liefert Befunde in drei
Schweregraden (**kritisch / prüfen / Hinweis**) mit Kapitel-Referenz und
Gruppe-1/2-Konsequenz. Die Auswertung erscheint im PDF und in `/api/answers/`;
`/api/gdt/result/` liefert die Zusammenfassung als Zählwerte. Sie ist
Entscheidungsunterstützung – die abschließende Beurteilung trifft die Ärztin/der Arzt.

## Schnellstart

### Mit Docker Compose (empfohlen)

```bash
cp .env.example .env    # Werte setzen! DJANGO_SECRET_KEY und ADMIN_API_KEY sind Pflicht
docker-compose up --build
docker-compose exec backend python manage.py createsuperuser
```

- Frontend: http://localhost:3000
- Backend-API: http://localhost:8000/api/
- Django-Admin: http://localhost:8000/admin/
- Praxis-Admin (Sessions/Einladungen): http://localhost:3000/admin

### Lokale Entwicklung

Ohne Docker/PostgreSQL: `USE_SQLITE=True` in `backend/.env` setzen — dann läuft
alles gegen `backend/db.sqlite3`. **Wichtig:** immer das venv aktivieren, sonst
fehlt dem globalen Python u.a. `psycopg` (`ModuleNotFoundError: No module named
'psycopg'`).

```powershell
# Backend (PowerShell, Windows)
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1                     # Pfad ist "venv", nicht ".venv"
pip install -r requirements.txt
copy .env.example .env                          # dann USE_SQLITE=True setzen
python manage.py migrate
python manage.py load_catalog
python manage.py create_sample_data             # optional: Test-Session + Token
python manage.py runserver

# Frontend (zweites Terminal)
cd frontend
npm install
copy .env.example .env.local                    # BACKEND_URL=http://localhost:8000
npm run dev
```

Danach den Token aus `create_sample_data` aufrufen: `http://localhost:3000/q/<TOKEN>`.
Praxis-Admin unter `http://localhost:3000/admin` mit dem `ADMIN_API_KEY` aus der `.env`.

## Projektstruktur

```
fragebogen/
├── backend/
│   ├── config/                  # Django-Konfiguration
│   └── questionnaires/          # Modelle, API-Views, Serializer, Admin
│       └── management/commands/ # create_sample_data, create_completed_session,
│                                # purge_sessions (DSGVO-Retention)
├── frontend/
│   ├── app/
│   │   ├── q/[token]/           # Patienten-Fragebogen
│   │   ├── admin/               # Praxis-Admin (API-Key-Login)
│   │   ├── print/[token]/       # Serverseitige Druckvorlage
│   │   └── api/puppeteer-pdf/   # Design-PDF-Route (Chromium)
│   ├── components/              # Formular, Sidebar, shadcn/ui
│   └── lib/ess.ts               # ESS-Fragen & Auswertung (eine Quelle)
├── gdt_bridge/                  # Windows-Dienst für SAMAS (GDT 2.1)
├── docker-compose.yml           # Produktion
├── docker-compose.dev.yml       # Entwicklung (db einzeln startbar)
└── deploy.bat                   # Push + Server-Update per SSH
```

## API-Endpunkte

### Patient (Token-basiert)
- `GET  /api/session/<token>/` – Session-Details (410 wenn abgelaufen/ausgefüllt)
- `POST /api/submit/<token>/` – Fragebogen einreichen (atomar, Doppel-Submit → 400)
- `GET  /api/answers/<token>/` – Antworten + Schema + Auswertung für die Print-Page (410 nach Ablauf)

### Praxis-Admin (Header `Authorization: Bearer <ADMIN_API_KEY>`)
- `GET/POST /api/admin/sessions/` – Sessions auflisten / anlegen (+ Einladungs-Mail)
- `PATCH  /api/admin/sessions/<token>/update/` – Patientendaten ändern
- `POST   /api/admin/sessions/<token>/resend/` – Einladung erneut senden (verlängert Gültigkeit)
- `DELETE /api/admin/sessions/<token>/delete/` – Session löschen

### GDT-Bridge (gleicher API-Key)
- `POST /api/gdt/session/` – Session aus GDT-Anforderung anlegen
- `GET  /api/gdt/result/<token>/` – Ergebnis abfragen (202 = offen, 410 = abgelaufen)

## ESS (Epworth Sleepiness Scale)

- **0–9 Punkte:** Normal
- **10–15 Punkte:** Erhöht – weitere Abklärung empfohlen
- **≥16 Punkte:** Ausgeprägt – ärztliche Abklärung erforderlich

Die Auswertung wird serverseitig berechnet (`serializers.py`); das Frontend zeigt
denselben Score live an (`lib/ess.ts`).

## GDT-Bridge (SAMAS-Anbindung)

Windows-Dienst auf dem Praxisrechner (`gdt_bridge/`, Installation über `install.bat`
als Administrator). Ablauf: SAMAS schreibt eine Anforderungs-GDT → Bridge legt per API
eine Session an → Link-GDT zurück an SAMAS → nach dem Ausfüllen Ergebnis-GDT mit
ESS-Score. Konfiguration in `config.ini` (Vorlage: `config.ini.example`), u.a.
`api_key` (= `ADMIN_API_KEY` des Servers) und `gdt_encoding` (Default cp1252,
GDT-Standard wäre cp437).

**Hinweis:** Das Feldmapping folgt dem GDT-Standard (FK 3101 = Nachname,
FK 3102 = Vorname). Vor dem ersten Praxiseinsatz mit einem echten SAMAS-Export
(inkl. Umlaut-Namen) verifizieren.

## Datenschutz & Retention

- Patienten sehen die Datenschutzhinweise im Einwilligungs-Schritt des Fragebogens.
- Ergebnis-Endpunkte (`answers`/`pdf`) liefern nach Ablauf des Links **410 Gone**.
- Abgelaufene Sessions werden per Management-Command gelöscht – als Cron/Task einrichten:

```bash
docker-compose exec backend python manage.py purge_sessions --days 30
```

- Die Bridge loggt keine Patientennamen und räumt `pending.json` automatisch auf.

## Sicherheit

- `DJANGO_SECRET_KEY` und `ADMIN_API_KEY` sind Pflicht (Compose bricht sonst ab) –
  niemals committen, nur in der lokalen `.env`.
- `DEBUG=False` ist der Default; nur für Entwicklung explizit auf `True` setzen.
- API-Key-Vergleich ist timing-sicher, alle anonymen Endpunkte sind gedrosselt.
- **Empfehlung:** TLS über einen Reverse-Proxy (z.B. Synology-Reverse-Proxy mit
  Let's Encrypt) terminieren und `APP_URL` auf die https-Adresse stellen – aktuell
  laufen Patientenlink und GDT-Bridge über Klartext-HTTP im LAN.

## Tests

```bash
cd backend
python manage.py test questionnaires   # 19 API-Tests (Submit, Katalog, Ablauf, Escaping, Auth, Purge)
```

```bash
cd frontend
npm run lint && npm run build
```

## Nützliche Kommandos

```bash
# Test-Session mit Token erzeugen
docker-compose exec backend python manage.py create_sample_data

# Ausgefüllte Test-Session (für PDF-Tests)
docker-compose exec backend python manage.py create_completed_session

# Logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Lizenz

Proprietär – nur für interne Verwendung.
