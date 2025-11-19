asas# 🚀 Complete Railway Deployment Guide

Deploy both your **Backend (Flask API)** and **Frontend (Static HTML/CSS/JS)** to Railway for FREE with $5 monthly credit!

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Deploy Backend to Railway](#deploy-backend-to-railway)
3. [Deploy Frontend to Railway](#deploy-frontend-to-railway)
4. [Connect Frontend to Backend](#connect-frontend-to-backend)
5. [Verify Deployment](#verify-deployment)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

Before you start, you need:

- ✅ **GitHub Account** (already have it - `aravind-gm`)
- ✅ **Railway Account** (free, created via GitHub)
- ✅ **Code pushed to GitHub** (`image-comparison-main` repo)
- ✅ **Backend files:** `api/app.py`, `api/comparison.py`, `api/model.py`
- ✅ **Frontend files:** `public/index.html`, `public/style.css`, `public/config.js`

---

## 🔧 Deploy Backend to Railway

### **Step 1: Sign Up for Railway**

1. Go to **https://railway.app**
2. Click **"Start Free"** button
3. Click **"Continue with GitHub"**
4. Authorize Railway to access your GitHub repos
5. You're in! ✅

### **Step 2: Create Backend Service**

1. Go to **https://railway.app/dashboard** (or click the Railway logo after login)
2. Click **"New Project"** button
3. Select **"Deploy from GitHub repo"**
4. Search for: `image-comparison-main`
5. Click **"Import"** (or "Select")
6. Railway will auto-detect your Python project ✅

### **Step 3: Configure Backend Service**

Railway should auto-detect your Python project. Here's what happens:

**Auto-detection:**
- ✅ Detects `requirements.txt` → installs all dependencies
- ✅ Detects `Procfile` → uses `gunicorn api.app:app --workers 1 --threads 2 --timeout 300`
- ✅ Sets PORT to 3000 (Railway default)

**Wait for deployment:**
- Building: ~3-5 minutes (installs PyTorch, dependencies)
- Deploying: ~1-2 minutes
- Starting: ~1 minute (loads MobileNetV2 model)

**Total time: ~5-8 minutes**

### **Step 4: Get Your Backend URL**

1. Go to your Railway project dashboard
2. Click on the **"web"** service (or your service name)
3. On the right side, look for **"Domains"** section
4. You'll see a URL like: `https://your-railway-app-production.up.railway.app`
5. **Copy this URL** - you'll need it for the frontend

### **Step 5: Test Backend is Running**

```bash
# Test your backend URL (replace with your actual URL)
curl https://your-railway-app-production.up.railway.app
```

**Expected response:**
```json
{
  "status": "running",
  "message": "NeuralVision AI Backend API",
  "version": "1.0.1",
  "model": "MobileNetV2",
  "memory_mb": 250.5,
  "endpoints": {
    "/api/compare": "POST - Compare two images",
    "/health": "GET - Detailed health check"
  }
}
```

**If you get 502/503:** Wait 2-3 more minutes. Railway is still loading the model.

✅ **Backend is now live!**

---

## 🎨 Deploy Frontend to Railway

You have **2 options**:

### **Option A: Deploy as Static Files on Railway (RECOMMENDED)**

#### **Step 1: Update Frontend Config**

Update `public/config.js` with your backend URL:

```javascript
// public/config.js
const CONFIG = {
    BACKEND_URL: 'https://your-railway-app-production.up.railway.app/api/compare',
};
```

Replace `your-railway-app-production.up.railway.app` with your actual backend URL from Step 4 above.

#### **Step 2: Create Static Site on Railway**

Option A1: Deploy `public/` as a separate service
1. Go to Railway dashboard
2. Click **"New"** button in your project
3. Select **"GitHub repo"**
4. Select `image-comparison-main` again
5. Now you'll have a choice - click **"Static Site"** or configure manually

**For a static site on Railway, you need a simple Node.js server. Create a file:**

**Create `server.js` in the root directory:**

```javascript
// server.js - Simple static file server for Railway
const express = require('express');
const path = require('path');
const app = express();

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html for all routes (single-page app support)
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`Frontend server running on port ${PORT}`);
});
```

**Create `package.json` in the root (if it doesn't exist):**

```json
{
  "name": "image-comparison-frontend",
  "version": "1.0.0",
  "description": "Frontend for NeuralVision AI Image Comparison",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

#### **Step 3: Deploy Frontend Service**

1. Push these files (`server.js`, `package.json`) to GitHub
2. Go to Railway dashboard
3. Click **"New"** button
4. Select **"Deploy from GitHub repo"**
5. Select the same `image-comparison-main` repo
6. Railway will detect `server.js` and deploy it as a Node.js service

#### **Step 4: Get Frontend URL**

1. After deployment, click on the Node.js service
2. Find the **"Domains"** section
3. Copy the URL: `https://your-frontend-production.up.railway.app`

✅ **Frontend is now live!**

---

### **Option B: Deploy Frontend to Netlify (ALTERNATIVE)**

If you prefer to keep frontend separate from Railway:

#### **Step 1: Push to GitHub**
```bash
git add .
git commit -m "Ready for Netlify deployment"
git push origin main
```

#### **Step 2: Deploy to Netlify**

1. Go to **https://netlify.com**
2. Click **"Sign up"** → **"Sign up with GitHub"**
3. Click **"New site from Git"**
4. Select your GitHub repo: `image-comparison-main`
5. Deploy settings:
   - **Base directory:** (leave empty)
   - **Build command:** (leave empty)
   - **Publish directory:** `public`
6. Click **"Deploy site"**

#### **Step 3: Update Frontend Config**

In `public/config.js`:
```javascript
const CONFIG = {
    BACKEND_URL: 'https://your-railway-backend.up.railway.app/api/compare',
};
```

#### **Step 4: Get Netlify URL**

Your Netlify site will have a URL like: `https://your-site-name.netlify.app`

---

## 🔗 Connect Frontend to Backend

### **For Option A (Both on Railway):**

1. **Update config.js:**
```javascript
// public/config.js
const CONFIG = {
    BACKEND_URL: 'https://your-backend-production.up.railway.app/api/compare',
};
```

2. **Commit and push:**
```bash
git add public/config.js
git commit -m "Update backend URL for Railway"
git push origin main
```

3. **Trigger redeploy in Railway:**
   - Go to your frontend service
   - Click **"Deploy"** or **"Redeploy"** button
   - Wait 1-2 minutes

### **For Option B (Backend on Railway, Frontend on Netlify):**

1. **Update config.js:**
```javascript
const CONFIG = {
    BACKEND_URL: 'https://your-backend-production.up.railway.app/api/compare',
};
```

2. **Commit and push:**
```bash
git add public/config.js
git commit -m "Update backend URL"
git push origin main
```

3. **Trigger Netlify redeploy:**
   - Go to Netlify dashboard
   - Your site will auto-redeploy on push
   - Check **"Deploys"** tab for status

---

## ✅ Verify Deployment

### **Test 1: Backend Health Check**

```bash
# Check if backend is running
curl https://your-backend-production.up.railway.app

# Check memory usage
curl https://your-backend-production.up.railway.app/health
```

**Expected response:**
```json
{
  "status": "running",
  "message": "NeuralVision AI Backend API",
  "model": "MobileNetV2"
}
```

### **Test 2: Open Frontend in Browser**

1. Open your frontend URL in a browser
   - **Option A:** `https://your-frontend-production.up.railway.app`
   - **Option B:** `https://your-site.netlify.app`

2. You should see your image comparison interface

3. **Upload two test images** and click "Compare"
   - If successful, you'll see a similarity score
   - If it fails, check browser console (F12) for errors

### **Test 3: Check Logs**

**For Backend:**
1. Go to Railway dashboard
2. Click your backend service
3. Go to **"Logs"** tab
4. Should show:
   ```
   Listening on port 3000
   model_loaded=True
   ```

**For Frontend (Option A):**
1. Go to Railway dashboard
2. Click your frontend service
3. Go to **"Logs"** tab
4. Should show:
   ```
   Frontend server running on port 3001
   ```

---

## 🔍 Troubleshooting

### **Problem: 502 Bad Gateway on Backend**

**Cause:** Model is still loading or out of memory

**Solution:**
1. Wait another 2-3 minutes
2. Check Railway logs for errors
3. If persists, Railway might need upgrade (currently using free tier)

**Check logs:**
- Go to Railway dashboard → Backend service → Logs
- Look for `model_loaded` or import errors

### **Problem: Frontend Shows "Failed to Fetch"**

**Cause:** CORS issue or backend URL is wrong

**Solution:**
1. Check `public/config.js` - is the backend URL correct?
2. Make sure backend URL has `/api/compare` at the end
3. Check backend is actually running (Test 1 above)

**Debug:**
- Open browser console (F12)
- Check network tab for failed requests
- Verify URL in Network tab matches your backend

### **Problem: Images Upload But Get Error**

**Cause:** Backend is out of memory

**Solution:**
1. Check Railway logs
2. Wait for service to restart (automatic)
3. If repeated, might need paid Railway plan

**Check logs:**
```bash
# Look for "killed" or "signal 9" in Railway logs
# This means out of memory
```

### **Problem: No Domains Showing in Railway**

**Solution:**
1. Wait 2-3 minutes for Railway to assign a domain
2. Go to service settings
3. Click **"Generate Domain"** button manually

### **Problem: Cannot Push to GitHub**

```bash
# Make sure you're in the right directory
cd c:\Users\selvi\Downloads\image-comparison-main

# Check status
git status

# Add files
git add .

# Commit
git commit -m "Deploy to Railway"

# Push
git push origin main
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────┐
│     Your Browser (User)                 │
└─────────────────┬───────────────────────┘
                  │
                  ├──► OPTION A (Recommended)
                  │    ┌──────────────────┐
                  │    │ Railway Frontend │
                  │    │ (Node.js Server)│
                  │    └─────────┬────────┘
                  │              │
                  └──► OPTION B
                       ┌──────────────────┐
                       │ Netlify Frontend │
                       │ (Static Site)    │
                       └────────┬─────────┘
                                │
                      ┌─────────▼──────────┐
                      │ Railway Backend    │
                      │ (Flask + PyTorch) │
                      │ • MobileNetV2      │
                      │ • Image Compare    │
                      └────────────────────┘
```

---

## 💰 Cost & Quotas

| Item | Limit |
|------|-------|
| **Monthly Credit** | $5 FREE |
| **RAM per Service** | 512MB-1GB |
| **Bandwidth** | Unlimited |
| **Build Time** | Unlimited |
| **Number of Services** | Unlimited |

**Typical Usage:** ~$1-2/month (well within $5 credit)

---

## 🚀 Quick Checklist

Before going live:

- [ ] Backend deployed to Railway ✅
- [ ] Backend URL copied
- [ ] `public/config.js` updated with backend URL
- [ ] Frontend deployed to Railway (Option A) or Netlify (Option B)
- [ ] Frontend URL obtained
- [ ] Tested backend with curl
- [ ] Tested frontend in browser
- [ ] Uploaded test images
- [ ] Verified similarity score works

---

## 📞 Support

**If something doesn't work:**

1. **Check Railway Status:** https://status.railway.app
2. **Check Netlify Status:** https://status.netlify.com
3. **Review Logs:** Each service has a Logs tab
4. **Wait:** Railway takes 5-8 minutes for first deployment
5. **Redeploy:** Click "Redeploy" button in Railway dashboard

---

## 🎉 Success!

Once everything is working:

1. Share your frontend URL with others
2. They can upload images and see similarity scores
3. Backend runs on Railway's infrastructure
4. Everything is automated and scalable
5. You're using the $5 free monthly credit

**Congratulations! Your app is deployed! 🚀**

---

## 📝 Additional Notes

### **Updating Code**

After deployment, updates are automatic:

1. Make changes to your code locally
2. Push to GitHub: `git push origin main`
3. Railway auto-detects the change (within 1-2 minutes)
4. Service automatically redeploys
5. No manual intervention needed

### **Scaling**

If you need more power later:

- **Backend:** Upgrade Railway plan ($7+/month) for more RAM/CPU
- **Frontend:** No upgrade needed (static files are always fast)

### **Custom Domain**

To use your own domain (optional):

1. Buy domain (GoDaddy, Namecheap, etc.)
2. In Railway → Settings → Domains → Add Custom Domain
3. Update DNS records (instructions in Railway)

---

**Last updated:** November 18, 2025
**Status:** Ready for Production ✅
