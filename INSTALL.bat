@echo off
echo ================================================
echo    Installing NeuralVision AI Dependencies
echo ================================================
echo.
echo Installing required Python packages...
echo This may take a few minutes...
echo.

cd /d "%~dp0"
pip install -r requirements.txt

echo.
echo ================================================
echo Installation complete!
echo ================================================
echo.
echo You can now run START_APP.bat to launch the application.
echo.
pause
