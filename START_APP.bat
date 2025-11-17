@echo off
title NeuralVision AI - Image Comparison App
color 0A

echo.
echo  ███╗   ██╗███████╗██╗   ██╗██████╗  █████╗ ██╗     
echo  ████╗  ██║██╔════╝██║   ██║██╔══██╗██╔══██╗██║     
echo  ██╔██╗ ██║█████╗  ██║   ██║██████╔╝███████║██║     
echo  ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██╔══██║██║     
echo  ██║ ╚████║███████╗╚██████╔╝██║  ██║██║  ██║███████╗
echo  ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
echo.
echo          Vision AI - Image Similarity Analyzer
echo  ========================================================
echo.
echo  Starting the complete application...
echo.
echo  [1/2] Starting Backend Flask Server...
cd /d "%~dp0"

REM Start backend in a new window
start "NeuralVision Backend" cmd /k "python api\app.py"

echo  [✓] Backend server starting on http://127.0.0.1:5000
echo.
echo  [2/2] Waiting 3 seconds for server to initialize...
timeout /t 3 /nobreak >nul

echo  [✓] Opening Frontend...
start "" "public\index.html"

echo.
echo  ========================================================
echo  ✓ Application started successfully!
echo  ========================================================
echo.
echo  Backend:  http://127.0.0.1:5000
echo  Frontend: Opened in your browser
echo.
echo  Team Lead: Aravind GM
echo  Team: Farha Nazz, Manayatha, Rithick, Pranav Jain
echo.
echo  ========================================================
echo  Press any key to stop the application...
echo  ========================================================
pause >nul

REM Kill the backend server when user presses a key
taskkill /FI "WindowTitle eq NeuralVision Backend*" /T /F >nul 2>&1
echo.
echo  Application stopped.
timeout /t 2 >nul
