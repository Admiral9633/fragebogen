@echo off
:: deploy.bat – neuen Code vom Git holen und Server aktualisieren
:: Im Fragebogen-Projektordner ausführen

setlocal
cd /d "%~dp0"

echo [1/4] Git Pull ...
git pull
if %errorLevel% NEQ 0 (
    echo FEHLER: git pull fehlgeschlagen.
    pause & exit /b 1
)

echo [2/4] Python Cache loeschen ...
for /d /r backend %%d in (__pycache__) do (
    if exist "%%d" rd /s /q "%%d"
)

echo [3/4] Backend neu starten ...
docker compose restart backend

echo [4/4] Warten und Status pruefen ...
timeout /t 5 /nobreak > nul
docker compose ps backend

echo.
echo Fertig! Server laeuft mit aktuellem Code.
pause
