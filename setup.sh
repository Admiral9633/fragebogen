#!/bin/bash

# Verkehrsmedizin App - Development Setup Script
# Dieses Script richtet die lokale Entwicklungsumgebung ein

set -e

echo "🚀 Verkehrsmedizin App Setup wird gestartet..."

# Farben für Output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Backend Setup
echo -e "\n${BLUE}📦 Backend Setup...${NC}"
cd backend

if [ ! -d "venv" ]; then
    echo "Erstelle virtuelle Umgebung..."
    python -m venv venv
fi

echo "Aktiviere virtuelle Umgebung und installiere Dependencies..."
source venv/bin/activate || source venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Kopiere .env.example zu .env..."
    cp .env.example .env
fi

cd ..

# 2. Frontend Setup
echo -e "\n${BLUE}📦 Frontend Setup...${NC}"
cd frontend

if [ ! -d "node_modules" ]; then
    echo "Installiere Node Dependencies..."
    npm install
fi

if [ ! -f ".env.local" ]; then
    echo "Kopiere .env.example zu .env.local..."
    cp .env.example .env.local
fi

cd ..

# 3. Datenbank Setup
echo -e "\n${BLUE}🗄️  Datenbank Setup...${NC}"
echo "Starte PostgreSQL Container..."
docker-compose -f docker-compose.dev.yml up -d

echo "Warte auf Datenbank..."
sleep 5

# 4. Django Migrationen
echo -e "\n${BLUE}🔄 Django Migrationen...${NC}"
cd backend
source venv/bin/activate || source venv/Scripts/activate
python manage.py migrate

echo -e "\n${GREEN}✅ Setup abgeschlossen!${NC}"
echo -e "\n${BLUE}Nächste Schritte:${NC}"
echo "1. Backend starten:"
echo "   cd backend && source venv/bin/activate && python manage.py runserver"
echo ""
echo "2. Frontend starten (neues Terminal):"
echo "   cd frontend && npm run dev"
echo ""
echo "3. Superuser erstellen:"
echo "   cd backend && source venv/bin/activate && python manage.py createsuperuser"
echo ""
echo "URLs:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8000/api/"
echo "  - Admin: http://localhost:8000/admin/"
