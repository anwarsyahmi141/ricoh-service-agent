@echo off
title Ricoh SC Guide Local Server
echo ========================================================
echo   RICOH SC DASHBOARD LOCAL WI-FI SERVER
echo ========================================================
echo.
echo Dashboard is now accessible on your office Wi-Fi / LAN!
echo Tell your clerk to open this URL in their browser:
echo.
echo    http://192.168.0.143:8080/
echo.
echo (Keep this window open while sharing. Press Ctrl+C to stop)
echo ========================================================
echo.
python -m http.server 8080 --directory "C:\Users\kaze\ricoh-service-agent"
pause
