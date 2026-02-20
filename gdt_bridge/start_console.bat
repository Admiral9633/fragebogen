@echo off
:: Startet die GDT Bridge direkt im Konsolenfenster (kein Windows Service nötig)
:: Zum Testen und Debuggen – Strg+C zum Stoppen
setlocal
set "SCRIPT_DIR=%~dp0"
echo GDT Bridge Konsolenmodus – Strg+C zum Stoppen
echo Log wird auch in bridge.log geschrieben
echo.
python "%SCRIPT_DIR%gdt_bridge_service.py" console
pause
