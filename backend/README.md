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

- `GET /api/session/<token>/` - Fragebogen-Session Details abrufen
- `POST /api/submit/<token>/` - Fragebogen einreichen
- `GET /api/pdf/<token>/` - PDF generieren

## Admin Interface

Admin-Interface ist verfügbar unter: `http://localhost:8000/admin/`
