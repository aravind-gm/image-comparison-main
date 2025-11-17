@echo off
echo ================================================
echo    Deploying NeuralVision AI to Vercel
echo ================================================
echo.
echo This will deploy your application to the cloud.
echo You'll get a public URL that anyone can access!
echo.
echo Prerequisites:
echo 1. Node.js must be installed
echo 2. You need a Vercel account (free)
echo.
pause

echo.
echo [Step 1/3] Installing Vercel CLI...
npm install -g vercel

echo.
echo [Step 2/3] Logging into Vercel...
echo (A browser window will open for authentication)
vercel login

echo.
echo [Step 3/3] Deploying application...
echo.
cd /d "%~dp0"
vercel --prod

echo.
echo ================================================
echo Deployment Complete!
echo ================================================
echo.
echo Your app is now live on the internet!
echo Copy the URL shown above to share with others.
echo.
pause
