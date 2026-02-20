@echo off
:: GDT Bridge – Deinstallation des Windows Service
:: Dieses Skript muss als Administrator ausgeführt werden!

setlocal
set "SCRIPT_DIR=%~dp0"

net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo FEHLER: Als Administrator ausfuhren!
    pause
    exit /b 1
)

echo Stoppe und entferne GDT Bridge Service ...
sc stop GdtBridgeService >nul 2>&1
timeout /t 2 /nobreak >nul
python "%SCRIPT_DIR%gdt_bridge_service.py" remove

echo Fertig.
pause
