@echo off
:: GDT Bridge – Installation als Windows Service
:: Dieses Skript muss als Administrator ausgeführt werden!

setlocal
set "SCRIPT_DIR=%~dp0"
set "SERVICE_SCRIPT=%SCRIPT_DIR%gdt_bridge_service.py"
set "CONFIG=%SCRIPT_DIR%config.ini"

echo ============================================================
echo  GDT Bridge – Windows Service Installation
echo ============================================================
echo.

:: Adminrechte prüfen
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo FEHLER: Dieses Skript muss als Administrator ausgefuhrt werden!
    echo Rechtsklick auf install.bat -> "Als Administrator ausfuhren"
    pause
    exit /b 1
)

:: config.ini prüfen
if not exist "%CONFIG%" (
    echo FEHLER: config.ini nicht gefunden!
    echo Kopiere config.ini.example zu config.ini und passe die Werte an.
    pause
    exit /b 1
)

:: Python prüfen
python --version >nul 2>&1
if %errorLevel% NEQ 0 (
    echo FEHLER: Python ist nicht installiert oder nicht im PATH.
    pause
    exit /b 1
)

:: Abhängigkeiten installieren
echo [1/4] Installiere Python-Abhängigkeiten ...
python -m pip install -r "%SCRIPT_DIR%requirements.txt" --quiet
if %errorLevel% NEQ 0 (
    echo FEHLER: pip install fehlgeschlagen.
    pause
    exit /b 1
)

:: pywin32 Post-Install
echo [2/4] Konfiguriere pywin32 ...
python -m win32com.client >nul 2>&1
python "%SystemRoot%\system32\cmd.exe" /c "python -c \"import win32serviceutil\"" >nul 2>&1

:: GDT-Ordner anlegen
echo [3/4] Lege GDT-Ordner an ...
for /f "tokens=2 delims==" %%A in ('findstr /i "gdt_inbox" "%CONFIG%"') do (
    set "INBOX=%%A"
)
for /f "tokens=2 delims==" %%A in ('findstr /i "gdt_outbox" "%CONFIG%"') do (
    set "OUTBOX=%%A"
)
set "INBOX=%INBOX: =%"
set "OUTBOX=%OUTBOX: =%"
if defined INBOX  mkdir "%INBOX%"  2>nul && echo    Inbox:  %INBOX%
if defined OUTBOX mkdir "%OUTBOX%" 2>nul && echo    Outbox: %OUTBOX%

:: Service registrieren und starten
echo [4/4] Registriere und starte Windows Service ...
python "%SERVICE_SCRIPT%" install
if %errorLevel% NEQ 0 (
    echo FEHLER: Service-Installation fehlgeschlagen.
    pause
    exit /b 1
)

:: Automatischen Start konfigurieren
sc config GdtBridgeService start= auto >nul
sc description GdtBridgeService "GDT Bridge – Fragebogen SAMAS Schnittstelle (Dr. Micka)" >nul

python "%SERVICE_SCRIPT%" start
if %errorLevel% NEQ 0 (
    echo WARNUNG: Service konnte nicht gestartet werden. Manuell starten: sc start GdtBridgeService
) else (
    echo Service erfolgreich gestartet.
)

echo.
echo ============================================================
echo  Installation abgeschlossen!
echo  Log-Datei: %SCRIPT_DIR%bridge.log
echo  Status:    sc query GdtBridgeService
echo  Stop:      sc stop GdtBridgeService
echo  Start:     sc start GdtBridgeService
echo ============================================================
pause
