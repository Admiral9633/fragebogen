@echo off
:: deploy.bat – Code pushen und Server per SSH aktualisieren

setlocal
cd /d "%~dp0"

set SSH_HOST=bjoern@192.168.178.84
set PROJ=/volume1/docker/fragebogen

echo [1/4] Git Push ...
git push
if %errorLevel% NEQ 0 (
    echo FEHLER: git push fehlgeschlagen.
    pause & exit /b 1
)

echo [2/4] Git Pull auf Server ...
ssh %SSH_HOST% "cd %PROJ% && git pull"
if %errorLevel% NEQ 0 (
    echo FEHLER: git pull auf Server fehlgeschlagen.
    pause & exit /b 1
)

echo [3/4] Python Cache loeschen + Backend neu starten ...
ssh %SSH_HOST% "find %PROJ%/backend -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; cd %PROJ% && docker compose restart backend"

echo [4/4] Status pruefen ...
timeout /t 5 /nobreak > nul
ssh %SSH_HOST% "cd %PROJ% && docker compose ps backend"

echo.
echo Fertig! Server laeuft mit aktuellem Code.
pause
