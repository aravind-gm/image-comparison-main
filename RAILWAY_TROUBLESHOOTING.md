# 🔧 Railway Deployment - Troubleshooting Decision Tree

Use this to diagnose and fix deployment issues quickly!

---

## 🚨 MAIN SYMPTOM: "502 Bad Gateway" from Backend

```
Start Here: Are you getting 502 error?
│
├─ YES → "Service is currently unavailable"
│        │
│        ├─ Check: How long has it been?
│        │   ├─ Less than 5 minutes?
│        │   │  └─ NORMAL: Just starting up
│        │   │     └─ ACTION: Wait 2-3 minutes, refresh
│        │   │
│        │   ├─ 5-10 minutes?
│        │   │  └─ Model loading
│        │   │     └─ ACTION: Wait another 2 minutes
│        │   │
│        │   └─ More than 10 minutes?
│        │      └─ Something's wrong
│        │         └─ ACTION: Go to next step
│        │
│        ├─ Check: What do logs say?
│        │   ├─ In Railway → Service → Logs
│        │   ├─ Look for errors
│        │   └─ See troubleshooting below
│        │
│        └─ Still not working?
│           └─ ACTION: → See "502 Solutions" below
│
└─ NO → "Getting valid response"
        └─ Skip to other sections
```

---

## 🛠️ 502 Bad Gateway - Solutions

### **Level 1: Wait & Refresh** (Try First)
```
1. Check Railway dashboard logs
   └─ Service → Logs tab
   
2. Look for:
   ├─ "Building successful" ✅
   ├─ "Booting worker" ✅
   ├─ "Model loaded" ✅
   └─ "Listening on 0.0.0.0:3000" ✅

3. If you see these → Wait 1-2 more minutes

4. Refresh browser: F5

5. Try: curl https://your-backend-url
```

**Outcome:**
- ✅ Works? → Proceed to test frontend
- ❌ Still 502? → Go to Level 2

---

### **Level 2: Check What's Wrong**

#### **Check 1: Out of Memory (OOM)**

**Symptoms in logs:**
```
signal 9 (SIGKILL) (TERM)
killed (signal 9)
signal: killed
```

**Diagnosis:** Model is too large or processes aren't cleaning up

**Solutions:**
1. Check Railway logs for "killed"
2. If seen:
   - Option A: Restart service manually
     - Railway → Service → "Manual Deploy"
     - Click "Clear build cache & deploy"
   - Option B: Wait for auto-restart (5 minutes)
   - Option C: Upgrade Railway plan ($7/month)
     - Go to Settings → Instance Type → Select "Starter"

**Test after fix:**
```bash
curl https://your-backend-url/health
# Should show memory usage ~250MB
```

---

#### **Check 2: Import Error**

**Symptoms in logs:**
```
ModuleNotFoundError: No module named 'torch'
ImportError: cannot import name 'compare_images'
No module named 'PIL'
```

**Diagnosis:** Dependency not installed

**Solutions:**
1. Check requirements.txt has all dependencies:
   ```
   Flask
   Flask-CORS
   torch
   torchvision
   numpy
   scipy
   Pillow
   opencv-python
   gunicorn
   psutil
   ```

2. If missing any:
   - Edit requirements.txt
   - Add missing package
   - Push to GitHub: `git push origin main`
   - Railway auto-rebuilds (5-8 min)

3. Manually trigger rebuild:
   - Railway → Service → "Manual Deploy"
   - Click "Rebuild and Redeploy"

**Test after fix:**
```bash
curl https://your-backend-url
# Should return JSON with "status": "running"
```

---

#### **Check 3: Port Binding Error**

**Symptoms in logs:**
```
Address already in use
Cannot bind to port 3000
OSError: [Errno 48] Address already in use
```

**Diagnosis:** Previous process still holding port

**Solutions:**
1. Railway → Service → Settings
2. Click "Restart service" button
3. Wait 30 seconds
4. Try again: `curl https://your-backend-url`

**Test after fix:**
```bash
curl https://your-backend-url
```

---

#### **Check 4: Gunicorn Timeout**

**Symptoms in logs:**
```
Worker timeout (timeout=300)
Worker (pid:XX) killed (signal 9)
```

**Diagnosis:** Request took too long

**Solutions:**
1. This is rare - happens when model load is very slow
2. Procfile already has 300s timeout (already optimized)
3. Increase if needed:
   ```
   web: gunicorn api.app:app --workers 1 --threads 2 --timeout 600 --max-requests 1000
   ```
4. Push to GitHub
5. Railway auto-rebuilds

---

### **Level 3: Nuclear Option** (Last Resort)

If nothing else works:

```
1. Go to Railway dashboard
2. Find your service
3. Click "Settings"
4. Click "Delete service" ❌
5. Go back to project
6. Click "New" button
7. Deploy from GitHub again
8. Fresh start (5-8 min)

This fixes ~99% of problems because:
├─ Clears all old processes
├─ Fresh dependency installation
├─ New environment
└─ Guaranteed clean state
```

---

## 🚨 Frontend Issue: "Failed to Fetch" Error

```
Start Here: Browser shows "Failed to Fetch"
│
├─ Check 1: Backend URL correct?
│   │
│   ├─ Open: public/config.js
│   ├─ Find: BACKEND_URL
│   ├─ Is it: 'https://your-backend-url.up.railway.app/api/compare'?
│   │
│   ├─ NO → Fix it!
│   │    ├─ Update correct backend URL
│   │    ├─ Save file
│   │    ├─ git add public/config.js
│   │    ├─ git commit -m "Fix backend URL"
│   │    ├─ git push origin main
│   │    ├─ Wait 2 minutes (frontend redeploying)
│   │    └─ Try again
│   │
│   └─ YES → Go to Check 2
│
├─ Check 2: Backend actually running?
│   │
│   ├─ Test: curl https://your-backend-url
│   │
│   ├─ NO (502/503) → Go fix backend first!
│   │    └─ Use "502 Bad Gateway" section above
│   │
│   └─ YES (JSON response) → Go to Check 3
│
├─ Check 3: Correct URL endpoint?
│   │
│   ├─ Should end with: /api/compare
│   ├─ Not just: /api
│   ├─ Not just: /
│   │
│   ├─ Wrong? → Fix in config.js
│   └─ Correct? → Go to Check 4
│
├─ Check 4: Browser console errors?
│   │
│   ├─ Open DevTools: F12
│   ├─ Go to: "Console" tab
│   ├─ Look for: Red error messages
│   │
│   ├─ See CORS error? 
│   │  ├─ Backend may have CORS disabled
│   │  ├─ Check api/app.py has CORS enabled ✅
│   │  └─ Should have: CORS(app, resources={r"/*": {...}})
│   │
│   ├─ See network error?
│   │  └─ Go to "Network" tab and try again
│   │     └─ Click failed request and check URL
│   │
│   └─ See other error?
│      └─ Search error message for specific help
│
└─ Still broken?
   └─ ACTION: → See "Failed to Fetch Solutions"
```

---

## 🔧 Failed to Fetch - Solutions

### **Solution 1: Update Backend URL**

**In:** `public/config.js`

**Change from:**
```javascript
BACKEND_URL: 'https://your-backend-url.up.railway.app/api/compare'
```

**To:** (use YOUR actual backend URL)
```javascript
BACKEND_URL: 'https://neuralvision-ai-production.up.railway.app/api/compare'
```

**Then:**
```bash
git add public/config.js
git commit -m "Fix backend URL"
git push origin main
# Wait 2 minutes for Railway to redeploy
```

---

### **Solution 2: Enable CORS on Backend**

**File:** `api/app.py`

**Check:** You have this code:
```python
from flask_cors import CORS

CORS(app, 
     resources={r"/*": {
         "origins": "*",
         "methods": ["GET", "POST", "OPTIONS", "PUT", "DELETE"],
         "allow_headers": ["Content-Type", "Authorization"],
     }}
)
```

**If missing:**
1. Edit `api/app.py`
2. Add the CORS import and configuration
3. Push: `git push origin main`
4. Railway rebuilds (1 min)

---

### **Solution 3: Check Request Format**

**Frontend should send:**
```
POST https://backend-url/api/compare
Content-Type: multipart/form-data

Form data:
├─ image1: <file object>
└─ image2: <file object>
```

**In:** `public/index.html` or your JS file

**Check:** File upload code looks like:
```javascript
const formData = new FormData();
formData.append('image1', file1);
formData.append('image2', file2);

fetch(CONFIG.BACKEND_URL, {
    method: 'POST',
    body: formData
})
```

---

## 🎨 Frontend Issue: Page Not Loading

```
Start Here: Frontend URL returns "Not Found" or blank
│
├─ Check 1: Frontend service running?
│   │
│   ├─ Railway → Frontend Service
│   ├─ Check "Domains" section
│   ├─ Does URL exist?
│   │
│   ├─ NO → Service didn't deploy
│   │    ├─ Check Logs tab
│   │    └─ Look for errors
│   │
│   └─ YES → Go to Check 2
│
├─ Check 2: Server.js exists?
│   │
│   ├─ In GitHub:
│   ├─ Root folder (not api/ folder)
│   ├─ File: server.js
│   │
│   ├─ NO → Create it!
│   │    ├─ Copy server.js content from guide
│   │    ├─ Save in root
│   │    ├─ git add server.js
│   │    ├─ git push origin main
│   │    └─ Wait 5 min, Railway rebuilds
│   │
│   └─ YES → Go to Check 3
│
├─ Check 3: package.json exists?
│   │
│   ├─ In GitHub:
│   ├─ Root folder (not api/ folder)
│   ├─ File: package.json
│   │
│   ├─ NO → Create it!
│   │    ├─ Copy package.json from guide
│   │    ├─ Save in root
│   │    ├─ git add package.json
│   │    ├─ git push origin main
│   │    └─ Wait 5 min, Railway rebuilds
│   │
│   └─ YES → Go to Check 4
│
├─ Check 4: Start command correct?
│   │
│   ├─ Railway → Frontend Service → Settings
│   ├─ Check: "Start command"
│   ├─ Should be: "node server.js"
│   │
│   ├─ Wrong? → Edit and save
│   ├─ Manual Deploy to apply
│   │
│   └─ YES → Go to Check 5
│
└─ Check 5: Check Logs
    │
    ├─ Railway → Frontend Service → Logs
    ├─ Look for: errors or warnings
    │
    ├─ See errors?
    │  └─ Note the error message
    │     └─ Search for specific troubleshooting
    │
    └─ No errors but still not loading?
       └─ ACTION: → "Not Loading Solutions"
```

---

## 📊 Frontend Not Loading - Solutions

### **Solution 1: Recreate Files**

**server.js** (copy exactly):
```javascript
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`Frontend server running on port ${PORT}`);
});
```

**package.json** (copy exactly):
```json
{
  "name": "image-comparison-frontend",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.2"
  },
  "scripts": {
    "start": "node server.js"
  }
}
```

---

### **Solution 2: Manual Redeploy**

1. Go to Railway dashboard
2. Click Frontend Service
3. Click "Deploy" button
4. Select "Redeploy" or "Rebuild and Redeploy"
5. Wait 5 minutes

---

### **Solution 3: Rebuild from Scratch**

Last resort:
1. Railway → Frontend Service → Settings
2. Delete service
3. Go back to project
4. Click "New"
5. Deploy from GitHub again
6. Wait 5-8 minutes

---

## 📈 Performance Issues: Slow Response

```
Start Here: Comparison takes too long
│
├─ Check: Response time
│   │
│   ├─ Less than 5 seconds?
│   │  └─ NORMAL for first request (model loading)
│   │     └─ Second request should be ~2 seconds
│   │
│   ├─ More than 10 seconds?
│   │  └─ Something's wrong
│   │     └─ Go to next checks
│   │
│   └─ Random slowness?
│      └─ Might be Railway overloaded
│         └─ Wait a minute and try again
│
├─ Check: Backend health
│   │
│   ├─ curl https://your-backend-url/health
│   │
│   ├─ Check: memory_mb value
│   │   ├─ > 400MB? → Getting full
│   │   ├─ < 250MB? → Normal
│   │   └─ Growing over time? → Memory leak
│   │
│   └─ Check: response_time
│       ├─ > 5 sec? → Overloaded
│       └─ < 2 sec? → Good
│
├─ Check: Image sizes
│   │
│   ├─ Very large images?
│   │  ├─ > 10MB each?
│   │  └─ Try smaller images (< 5MB)
│   │
│   └─ Normal size?
│      └─ Processing might just be slow
│         └─ Normal for MobileNetV2
│
└─ Still slow?
   └─ ACTION: → See "Performance Solutions"
```

---

## ⚡ Performance - Solutions

### **Solution 1: Check Image Sizes**
- Use images < 5MB each
- Try JPEG instead of PNG
- Lower resolution if possible

### **Solution 2: Memory Check**
```bash
curl https://your-backend-url/health
```

If memory > 400MB:
- Wait for auto-cleanup (1 min)
- Or restart service manually

### **Solution 3: Restart Backend**
1. Railway → Backend Service
2. Click "Restart service"
3. Wait 30 seconds
4. Try again

### **Solution 4: Clear Browser Cache**
```
Ctrl + Shift + Delete
Clear: All time
Select: Cache, Cookies
```

---

## 🎯 Complete Diagnostic Flow

```
Problem occurs
│
├─ What's the symptom?
│  │
│  ├─ "502 Bad Gateway" → See "502 Solutions"
│  ├─ "Failed to Fetch" → See "Failed to Fetch Solutions"
│  ├─ Frontend won't load → See "Frontend Not Loading Solutions"
│  ├─ Slow response → See "Performance Solutions"
│  ├─ Images not uploading → See "Upload Issues" below
│  └─ Other → See "Other Issues" below
│
├─ Check logs
│  ├─ Railway → Service → Logs
│  ├─ Copy error message
│  └─ Search below for that error
│
├─ Try solution
│  └─ Follow step-by-step
│
├─ Test fix
│  ├─ Refresh browser
│  ├─ Try again
│  └─ Does it work?
│
├─ YES ✅
│  └─ Done! Document what worked
│
└─ NO ❌
   ├─ Try next solution
   ├─ Or go to "Contact Support"
   └─ Include:
      ├─ Error message
      ├─ URLs (backend + frontend)
      ├─ Browser console errors
      └─ Railway logs
```

---

## 💬 Common Error Messages

| Error Message | Meaning | Fix |
|---------------|---------|-----|
| `ModuleNotFoundError` | Missing Python package | Update requirements.txt |
| `502 Bad Gateway` | Backend crashed | Wait or restart |
| `CORS error` | Frontend can't reach backend | Check backend URL |
| `Failed to fetch` | Network request failed | Check backend is running |
| `Cannot find module` | Missing Node package | Already fixed (express) |
| `Address already in use` | Port conflict | Restart service |
| `signal 9 (SIGKILL)` | Out of memory | Upgrade plan |
| `Connection refused` | Backend not running | Wait or restart |
| `404 Not Found` | URL wrong or file missing | Check path |

---

## 📞 Contact Support

If you're completely stuck:

1. **Gather info:**
   - Backend URL
   - Frontend URL
   - Complete error message
   - What you tried
   - Railway logs (copy 50 lines)

2. **Where to ask:**
   - Railway Docs: https://docs.railway.app
   - Railway Support: https://railway.app/support
   - Stack Overflow tag: railway.app
   - GitHub Issues: aravind-gm/image-comparison-main

3. **In message, include:**
   ```
   Problem: [describe]
   Error: [exact message]
   Backend: [your URL]
   Tried: [what you did]
   Logs: [relevant lines]
   ```

---

**Last Updated:** November 18, 2025  
**Covers:** Most common Railway deployment issues
