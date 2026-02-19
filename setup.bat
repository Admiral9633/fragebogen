@echo off
REM Verkehrsmedizin App - Development Setup Script (Windows)
REM Dieses Script richtet die lokale Entwicklungsumgebung ein

echo.
echo ======================================
echo Verkehrsmedizin App Setup
echo ======================================
echo.

REM 1. Backend Setup
echo [1/4] Backend Setup...
cd backend

if not exist "venv\" (
    echo Erstelle virtuelle Umgebung...
    python -m venv venv
)

echo Aktiviere virtuelle Umgebung und installiere Dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

if not exist ".env" (
    echo Kopiere .env.example zu .env...
    copy .env.example .env
)

cd ..

REM 2. Frontend Setup
echo.
echo [2/4] Frontend Setup...
cd frontend

if not exist "node_modules\" (
    echo Installiere Node Dependencies...
    call npm install
)

if not exist ".env.local" (
    echo Kopiere .env.example zu .env.local...
    copy .env.example .env.local
)

cd ..

REM 3. Datenbank Setup
echo.
echo [3/4] Datenbank Setup...
echo Starte PostgreSQL Container...
docker-compose -f docker-compose.dev.yml up -d

echo Warte auf Datenbank...
timeout /t 5 /nobreak > nul

REM 4. Django Migrationen
echo.
echo [4/4] Django Migrationen...
cd backend
call venv\Scripts\activate.bat
python manage.py migrate
cd ..

echo.
echo ======================================
echo Setup abgeschlossen!
echo ======================================
echo.
echo Naechste Schritte:
echo.
echo 1. Backend starten:
echo    cd backend
echo    venv\Scripts\activate
echo    python manage.py runserver
echo.
echo 2. Frontend starten (neues Terminal):
echo    cd frontend
echo    npm run dev
echo.
echo 3. Superuser erstellen:
echo    cd backend
echo    venv\Scripts\activate
echo    python manage.py createsuperuser
echo.
echo URLs:
echo   - Frontend: http://localhost:3000
echo   - Backend API: http://localhost:8000/api/
echo   - Admin: http://localhost:8000/admin/
echo.
pause
