@echo off
echo ================================================
echo    NeuralVision AI - Starting Backend Server
echo ================================================
echo.
echo Starting Flask API on port 5000...
echo.

cd /d "%~dp0"
python api\app.py

pause
