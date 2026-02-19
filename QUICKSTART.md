# Quick Start Guide

## Option 1: Docker Compose (Schnellster Start)

```bash
# Alle Services starten
docker-compose up --build

# In neuem Terminal: Superuser erstellen
docker-compose exec backend python manage.py createsuperuser

# Test-Daten erstellen
docker-compose exec backend python manage.py create_sample_data
```

Fertig! Öffne: http://localhost:3000

## Option 2: Lokale Entwicklung (Windows)

```bash
# Setup ausführen
setup.bat

# Backend starten (Terminal 1)
cd backend
venv\Scripts\activate
python manage.py runserver

# Frontend starten (Terminal 2)
cd frontend
npm run dev

# Superuser erstellen (Terminal 3)
cd backend
venv\Scripts\activate
python manage.py createsuperuser

# Test-Daten erstellen
python manage.py create_sample_data
```

## Option 3: Lokale Entwicklung (Linux/Mac)

```bash
# Setup ausführen
chmod +x setup.sh
./setup.sh

# Backend starten (Terminal 1)
cd backend
source venv/bin/activate
python manage.py runserver

# Frontend starten (Terminal 2)
cd frontend
npm run dev

# Superuser erstellen (Terminal 3)
cd backend
source venv/bin/activate
python manage.py createsuperuser

# Test-Daten erstellen
python manage.py create_sample_data
```

## URLs nach dem Start

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000/api/
- **Admin:** http://localhost:8000/admin/
- **Fragebogen:** http://localhost:3000/q/[TOKEN]

## Test-Workflow

1. Im Admin einloggen: http://localhost:8000/admin/
2. Neue Session erstellen oder `create_sample_data` Command nutzen
3. Token kopieren
4. Frontend aufrufen: http://localhost:3000/q/[TOKEN]
5. Fragebogen ausfüllen
6. PDF herunterladen

## Häufige Probleme

### Port bereits belegt
```bash
# Backend Port ändern
python manage.py runserver 8001

# Frontend Port ändern
npm run dev -- -p 3001
```

### Docker-Fehler
```bash
# Container neu bauen
docker-compose down -v
docker-compose up --build
```

### Datenbank-Fehler
```bash
# Migrations zurücksetzen
cd backend
python manage.py migrate --run-syncdb
```
