# Railway Deployment Checklist - Print & Follow

## 📋 Pre-Deployment (Before Starting)

### Files Check
- [ ] `server.js` exists in root folder
- [ ] `package.json` exists in root folder  
- [ ] `Procfile` exists in root folder
- [ ] `requirements.txt` has all packages
- [ ] `public/config.js` exists
- [ ] `api/app.py` exists
- [ ] `api/comparison.py` exists
- [ ] `api/model.py` exists

### GitHub Check
- [ ] All code committed: `git status` (shows nothing)
- [ ] Ready to push: `git log` (shows your commits)
- [ ] Remote set: `git remote -v` (shows github.com link)

### Documentation Check
- [ ] Read RAILWAY_QUICK_REFERENCE.md (5 min)
- [ ] Have backend URL format ready
- [ ] Have frontend URL format ready

---

## 🚀 Phase 1: Deploy Backend (5-8 minutes)

### Step 1: Push to GitHub
```bash
cd c:\Users\selvi\Downloads\image-comparison-main
git add .
git commit -m "Deploy to Railway"
git push origin main
```
- [ ] Code pushed successfully
- [ ] Check: https://github.com/aravind-gm/image-comparison-main (see new files)

### Step 2: Create Railway Account
- [ ] Go to https://railway.app
- [ ] Click "Start Free"
- [ ] Click "Continue with GitHub"
- [ ] Authorize Railway
- [ ] Accept $5 monthly credit

### Step 3: Create Project
- [ ] On Dashboard, click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Search for "image-comparison-main"
- [ ] Click "Import" or "Select"
- [ ] Click "Deploy"

### Step 4: Wait for Build
- [ ] Watch Logs tab in Railway dashboard
- [ ] Should see:
  - [ ] "Building..." message
  - [ ] "Installing dependencies"
  - [ ] "Downloading PyTorch"
  - [ ] "Starting Gunicorn"
  - [ ] "Listening on 0.0.0.0:3000"
- [ ] After ~5-8 minutes: Build complete

### Step 5: Get Backend URL
- [ ] Go to Backend Service
- [ ] Click "Domains" section on right
- [ ] Copy URL (example: `https://xxx-production.up.railway.app`)
- [ ] **Save this URL** - you'll need it!

### Step 6: Test Backend
```bash
curl https://YOUR-BACKEND-URL
```
- [ ] Response is JSON with "status": "running"
- [ ] Backend is working! ✅

---

## 🎨 Phase 2: Deploy Frontend (1-2 minutes)

Railway auto-detects frontend! (server.js + package.json)

### Step 1: Wait for Auto-Detection
- [ ] Go back to Railway project
- [ ] You should see TWO services now:
  - [ ] Backend (Python)
  - [ ] Frontend (Node.js)
- [ ] Frontend should deploy automatically

### Step 2: Get Frontend URL
- [ ] Click Frontend Service
- [ ] Click "Domains" section on right
- [ ] Copy URL (example: `https://yyy-production.up.railway.app`)
- [ ] **Save this URL** - you'll need it!

### Step 3: Test Frontend
- [ ] Open frontend URL in browser
- [ ] Should see your image upload form
- [ ] No errors in console (F12)

---

## 🔗 Phase 3: Connect Services (2 minutes)

### Step 1: Update Backend URL
**File:** `public/config.js`

**Find this line:**
```javascript
BACKEND_URL: 'https://your-backend-url.up.railway.app/api/compare',
```

**Replace with your actual backend URL:**
```javascript
BACKEND_URL: 'https://xxx-production.up.railway.app/api/compare',
```

- [ ] Updated correctly
- [ ] Added `/api/compare` at end

### Step 2: Push Changes
```bash
git add public/config.js
git commit -m "Update backend URL for Railway"
git push origin main
```
- [ ] Code pushed
- [ ] GitHub updated

### Step 3: Railway Auto-Redeploys
- [ ] Frontend service auto-detects change
- [ ] Watch Logs for "Redeploy" or "Deploy"
- [ ] Wait 1-2 minutes
- [ ] Should complete automatically

---

## ✅ Phase 4: Verification (5 minutes)

### Test 1: Backend Health
```bash
curl https://YOUR-BACKEND-URL/health
```
- [ ] Returns JSON
- [ ] Shows memory usage
- [ ] status: "healthy"

### Test 2: Frontend Loads
- [ ] Open frontend URL in browser
- [ ] See upload form
- [ ] No 404 or errors

### Test 3: Frontend to Backend Connection
- [ ] In browser, open DevTools (F12)
- [ ] Go to Console tab
- [ ] Upload two test images
- [ ] Click "Compare"
- [ ] Should NOT see errors
- [ ] Should see similarity score

### Test 4: Check Logs
- [ ] Railway → Backend Service → Logs
  - [ ] No "ERROR" messages
  - [ ] No "signal 9" (out of memory)
  - [ ] Should show requests
  
- [ ] Railway → Frontend Service → Logs
  - [ ] No errors
  - [ ] Should show "requests"

---

## 🎉 Success! You're Live!

### URLs to Share
- **Frontend:** `https://YOUR-FRONTEND-URL`
- **Backend:** `https://YOUR-BACKEND-URL` (no need to share this)

### Next Steps
- [ ] Test with real images
- [ ] Share frontend URL with others
- [ ] Monitor logs for issues
- [ ] Check `/health` endpoint occasionally

### Maintenance
- [ ] To update code: `git push` → Railway auto-redeploys
- [ ] To restart: Railway → Service → "Restart service"
- [ ] Monitor: Railway dashboard → Logs
- [ ] Health: Periodically check `/health` endpoint

---

## 🆘 Troubleshooting Quick Reference

| Problem | Quick Fix |
|---------|-----------|
| 502 Bad Gateway | Wait 3 more min, refresh |
| Failed to Fetch | Check backend URL in config.js |
| Frontend shows 404 | Check server.js exists |
| Images won't upload | Check browser console (F12) |
| Slow response | First request takes time, try again |
| Out of Memory | Restart service in Railway |

**For more help:** Read `RAILWAY_TROUBLESHOOTING.md`

---

## 📋 URLs You Need

| Item | Value | Status |
|------|-------|--------|
| Frontend URL | `https://...` | [ ] Get after deploy |
| Backend URL | `https://...` | [ ] Get after deploy |
| Health Check | `Backend-URL/health` | [ ] Test after deploy |
| API Endpoint | `Backend-URL/api/compare` | [ ] Used internally |

---

## 📞 Support Resources

- **Railway Docs:** https://docs.railway.app
- **Your Backend Health:** `https://YOUR-BACKEND-URL/health`
- **GitHub Repo:** https://github.com/aravind-gm/image-comparison-main
- **Railway Dashboard:** https://railway.app/dashboard

---

## ✨ Timeline

```
Expected Timing:
├─ Reading guides: 10 min
├─ GitHub push: 2 min
├─ Create project: 2 min
├─ Backend deploy: 5-8 min
├─ Frontend deploy: 1-2 min  
├─ Update config: 2 min
├─ Redeploy frontend: 1-2 min
├─ Testing: 5 min
└─ TOTAL: ~30-40 minutes

Active work: ~15 minutes
Waiting: ~15-25 minutes
```

---

**Print this page and check off each item as you go!** ✅

Last updated: November 18, 2025
Status: Ready for Production ✅
