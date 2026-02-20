@echo off
:: deploy.bat – Code pushen und Server per SSH aktualisieren
:: Voraussetzung: SSH-Key hinterlegt (ssh-copy-id bjoern@192.168.178.84)

setlocal
cd /d "%~dp0"

set SSH_HOST=bjoern@192.168.178.84
set PROJECT=/volume1/docker/fragebogen

echo [1/3] Git Push ...
git push
if %errorLevel% NEQ 0 (
    echo FEHLER: git push fehlgeschlagen.
    pause & exit /b 1
)

echo [2/3] Server: git pull + Cache loeschen + Neustart ...
ssh %SSH_HOST% "cd %PROJECT% && git pull && find backend -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; docker compose restart backend"
if %errorLevel% NEQ 0 (
    echo FEHLER: SSH-Verbindung fehlgeschlagen.
    echo Tipp: SSH-Key einrichten mit: ssh-copy-id %SSH_HOST%
    pause & exit /b 1
)

echo [3/3] Status pruefen ...
ssh %SSH_HOST% "cd %PROJECT% && docker compose ps backend"

echo.
echo Fertig! Server laeuft mit aktuellem Code.
pause
