# Verkehrsmedizin Backend

Django REST Framework Backend für das Verkehrsmedizin Fragebogen-System.

## Setup

1. Virtuelle Umgebung erstellen:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Dependencies installieren:
```bash
pip install -r requirements.txt
```

3. Umgebungsvariablen konfigurieren:
```bash
cp .env.example .env
# Bearbeite .env mit deinen Werten
```

4. Datenbank migrieren:
```bash
python manage.py migrate
```

5. Superuser erstellen:
```bash
python manage.py createsuperuser
```

6. Server starten:
```bash
python manage.py runserver
```

## API Endpoints

Vollständige Liste im [Projekt-README](../README.md#api-endpunkte). Kurzfassung:

- `GET /api/session/<token>/`, `POST /api/submit/<token>/`,
  `GET /api/pdf/<token>/`, `GET /api/answers/<token>/` – Patient (Token)
- `/api/admin/sessions/…` – Praxis-Admin (Header `Authorization: Bearer <ADMIN_API_KEY>`)
- `/api/gdt/…` – GDT-Bridge (gleicher API-Key)

## Tests

```bash
python manage.py test questionnaires
```

## Admin Interface

Admin-Interface ist verfügbar unter: `http://localhost:8000/admin/`
