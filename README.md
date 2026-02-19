# Verkehrsmedizin Fragebogen App

Vollständige Full-Stack-Anwendung für verkehrsmedizinische Fragebögen mit Epworth Sleepiness Scale (ESS).

## Technologie-Stack

### Backend
- Django 5.0
- Django REST Framework
- PostgreSQL 16
- WeasyPrint (PDF-Export)

### Frontend
- Next.js 15 (App Router)
- React 18
- Tailwind CSS
- Shadcn/ui Components
- React Hook Form

### Deployment
- Docker & Docker Compose
- Gunicorn (WSGI Server)
- PostgreSQL (Datenbank)

## Features

- ✅ Token-basierte Fragebogen-Sessions
- ✅ Epworth Sleepiness Scale (ESS) mit automatischer Auswertung
- ✅ Echtzeit-Score-Berechnung
- ✅ PDF-Export der Ergebnisse
- ✅ Responsive Design
- ✅ DSGVO-konforme Datenverarbeitung
- ✅ Session-Ablaufmanagement

## Schnellstart

### Mit Docker Compose (empfohlen)

1. **Projekt klonen und starten:**
```bash
cd Fragebogen
docker-compose up --build
```

2. **Backend initialisieren:**
```bash
# In einem neuen Terminal
docker-compose exec backend python manage.py createsuperuser
```

3. **Zugriff:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/

### Lokale Entwicklung

#### Backend Setup

```bash
cd backend

# Virtuelle Umgebung erstellen
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Dependencies installieren
pip install -r requirements.txt

# Umgebungsvariablen
cp .env.example .env

# Datenbank mit Docker starten
docker-compose -f ../docker-compose.dev.yml up -d

# Migrationen
python manage.py migrate

# Superuser erstellen
python manage.py createsuperuser

# Server starten
python manage.py runserver
```

#### Frontend Setup

```bash
cd frontend

# Dependencies installieren
npm install

# Umgebungsvariablen
cp .env.example .env.local

# Development Server
npm run dev
```

## Projektstruktur

```
Fragebogen/
├── backend/
│   ├── config/              # Django-Konfiguration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── questionnaires/      # Hauptapp
│   │   ├── models.py        # Datenmodelle
│   │   ├── serializers.py   # DRF Serializers
│   │   ├── views.py         # API Views
│   │   ├── urls.py          # URL-Routing
│   │   └── admin.py         # Admin-Interface
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app/                 # Next.js App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── q/[token]/       # Fragebogen-Seite
│   │       └── page.tsx
│   ├── components/          # React Components
│   │   ├── ui/              # Shadcn/ui Components
│   │   ├── ess-block.tsx    # ESS Fragebogen
│   │   └── questionnaire-form.tsx
│   ├── lib/                 # Utilities
│   │   ├── utils.ts
│   │   └── ess.ts           # ESS Logik
│   ├── package.json
│   ├── next.config.js
│   └── Dockerfile
│
├── docker-compose.yml       # Produktion
├── docker-compose.dev.yml   # Entwicklung
└── README.md
```

## API Endpoints

### Fragebogen-Session
- `GET /api/session/<token>/` - Session-Details abrufen
- `POST /api/submit/<token>/` - Fragebogen einreichen
- `GET /api/pdf/<token>/` - PDF generieren und herunterladen

### Beispiel-Request

```bash
# Session abrufen
curl http://localhost:8000/api/session/<TOKEN>/

# Fragebogen einreichen
curl -X POST http://localhost:8000/api/submit/<TOKEN>/ \
  -H "Content-Type: application/json" \
  -d '{
    "ess_1": 2,
    "ess_2": 1,
    "ess_3": 0,
    "ess_4": 2,
    "ess_5": 3,
    "ess_6": 0,
    "ess_7": 1,
    "ess_8": 0,
    "consent_complete": true,
    "consent_privacy": true
  }'
```

## ESS (Epworth Sleepiness Scale)

Die automatische Auswertung erfolgt nach folgenden Kriterien:

- **0-9 Punkte:** Normal - Keine erhöhte Tagesschläfrigkeit
- **10-15 Punkte:** Erhöht - Weitere Abklärung empfohlen
- **≥16 Punkte:** Ausgeprägt - Ärztliche Abklärung erforderlich

## Datenmodelle

### QuestionnaireTemplate
- Wiederverwendbare Fragebogen-Vorlagen
- Versionierung
- JSON-Schema für Flexibilität

### QuestionnaireSession
- Token-basierter Zugang
- Ablaufdatum (Standard: 7 Tage)
- Einmaliges Ausfüllen

### AnswerSet
- Gespeicherte Antworten
- ESS-Score und Kategorie
- Audit-Trail (Zeitstempel)

## Umgebungsvariablen

### Backend (.env)
```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_DB=verkehrsmedizin
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Deployment

### Produktion mit Docker Compose

1. **Umgebungsvariablen anpassen:**
   - Sicheres `DJANGO_SECRET_KEY` generieren
   - `DEBUG=False` setzen
   - Produktions-Domains in `ALLOWED_HOSTS` und `CORS_ALLOWED_ORIGINS`

2. **Container starten:**
```bash
docker-compose up -d
```

3. **Migrations und Static Files:**
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
docker-compose exec backend python manage.py createsuperuser
```

### Wichtige Sicherheitshinweise für Produktion

- ✅ Starke Passwörter für Datenbank
- ✅ HTTPS mit SSL/TLS Zertifikat
- ✅ Firewall-Regeln konfigurieren
- ✅ Regelmäßige Backups der Datenbank
- ✅ Secret Keys sicher speichern
- ✅ CORS nur für vertrauenswürdige Domains

## Entwicklung

### Neue Session erstellen (Django Shell)

```python
python manage.py shell

from questionnaires.models import QuestionnaireTemplate, QuestionnaireSession
from datetime import timedelta
from django.utils import timezone

# Template erstellen
template = QuestionnaireTemplate.objects.create(
    slug='verkehrsmedizin-v1',
    version=1,
    schema_json={'sections': ['ess']},
    is_active=True
)

# Session erstellen
session = QuestionnaireSession.objects.create(
    template=template,
    expires_at=timezone.now() + timedelta(days=7)
)

print(f"Token: {session.token}")
```

### Frontend testen

```bash
# Frontend-URL mit Token
http://localhost:3000/q/<TOKEN>
```

## Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## Troubleshooting

### Docker Container neustarten
```bash
docker-compose down
docker-compose up --build
```

### Datenbank zurücksetzen
```bash
docker-compose down -v
docker-compose up --build
```

### Logs anzeigen
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Lizenz

Proprietär - Nur für interne Verwendung

## Support

Bei Fragen oder Problemen wenden Sie sich an das Entwicklungsteam.

---

**Version:** 1.0  
**Erstellt am:** 18.02.2026  
**Letzte Aktualisierung:** 18.02.2026
