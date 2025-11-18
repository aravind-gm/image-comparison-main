@echo off
REM Quick Railway Deployment Script for Image Comparison App
REM This script guides you through deploying to Railway

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║  NeuralVision AI - Railway Deployment Assistant        ║
echo ╚════════════════════════════════════════════════════════╝
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git from https://git-scm.com
    pause
    exit /b 1
)

echo ✅ Git found. Proceeding with deployment...
echo.

REM Get current status
echo 📋 Checking git status...
git status

echo.
echo 🔄 Railway Deployment Steps:
echo.
echo Step 1: Push code to GitHub
echo   Command: git add . && git commit -m "Deploy to Railway" && git push origin main
echo.
echo Step 2: Go to https://railway.app
echo   - Sign up with GitHub
echo   - Click "New Project"
echo   - Select "Deploy from GitHub repo"
echo   - Choose: image-comparison-main
echo.
echo Step 3: Railway will auto-detect:
echo   ✅ Python project (from requirements.txt)
echo   ✅ Backend service (from Procfile)
echo   ✅ Frontend service (from server.js + package.json)
echo.
echo Step 4: Wait for deployment (5-8 minutes)
echo   - Backend will load MobileNetV2 model
echo   - Frontend will be served as static site
echo.
echo Step 5: Get your URLs:
echo   - Backend: https://your-project.up.railway.app
echo   - Frontend: https://your-frontend.up.railway.app
echo.
echo Step 6: Update config.js with backend URL
echo   - Open: public/config.js
echo   - Update: BACKEND_URL with your backend URL
echo   - Commit and push: git push origin main
echo.
echo Step 7: Test your app
echo   - Open frontend URL in browser
echo   - Upload two images
echo   - Click Compare and verify similarity score
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.

REM Ask if user wants to proceed with git push
set /p proceed="Do you want to commit and push to GitHub now? (y/n): "
if /i "%proceed%"=="y" (
    echo.
    echo 📤 Pushing to GitHub...
    git add .
    git commit -m "Deploy to Railway - Frontend and Backend"
    git push origin main
    
    if errorlevel 0 (
        echo.
        echo ✅ Code pushed successfully!
        echo.
        echo 🚀 Next steps:
        echo    1. Go to https://railway.app/dashboard
        echo    2. Click "New Project"
        echo    3. Select "Deploy from GitHub repo"
        echo    4. Choose "image-comparison-main"
        echo    5. Wait for deployment to complete
        echo.
    ) else (
        echo ❌ Git push failed. Check your credentials and try again.
    )
) else (
    echo.
    echo 📝 Remember to push your code to GitHub before deploying to Railway
    echo    Command: git push origin main
    echo.
)

echo.
echo 📚 For detailed guide, read: RAILWAY_DEPLOYMENT_GUIDE.md
echo.
pause
