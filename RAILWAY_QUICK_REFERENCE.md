# 🚀 Railway Deployment - Quick Reference

## ⚡ 5-Minute Quick Start

### **Step 1: Prepare Code (Local)**
```bash
cd c:\Users\selvi\Downloads\image-comparison-main
git add .
git commit -m "Deploy to Railway"
git push origin main
```

### **Step 2: Create Railway Account**
1. Go to https://railway.app
2. Click **"Start Free"**
3. Click **"Continue with GitHub"**
4. Authorize Railway
5. ✅ You have $5 monthly credit!

### **Step 3: Deploy Backend**
1. Click **"New Project"** on Railway dashboard
2. Select **"Deploy from GitHub repo"**
3. Search & select: `image-comparison-main`
4. Wait 5-8 minutes
5. Copy your backend URL from **"Domains"** section

### **Step 4: Update Frontend Config**
Edit `public/config.js`:
```javascript
const CONFIG = {
    BACKEND_URL: 'https://your-backend-url.up.railway.app/api/compare',
};
```

Push to GitHub:
```bash
git add public/config.js
git commit -m "Update backend URL"
git push origin main
```

Railway auto-redeploys. Done! ✅

---

## 📊 Architecture After Deployment

```
Internet
   │
   ├─ User Browser
   │  │
   │  └─ Railway Frontend (Node.js)
   │     URL: https://your-app-production.up.railway.app
   │     Serves: public/index.html, style.css, config.js
   │
   └─ Frontend makes requests to Backend
      │
      └─ Railway Backend (Python)
         URL: https://your-backend-production.up.railway.app
         • Flask API
         • MobileNetV2 Model
         • Image Comparison Logic
```

---

## 🔗 Important URLs

| Service | URL | Notes |
|---------|-----|-------|
| **Frontend** | `https://your-app-production.up.railway.app` | What users see |
| **Backend** | `https://your-backend-production.up.railway.app` | API endpoint |
| **Health Check** | `https://your-backend-production.up.railway.app/health` | Check if backend is running |
| **API Endpoint** | `https://your-backend-production.up.railway.app/api/compare` | Compare images (POST) |

---

## ✅ Verification Checklist

- [ ] Backend deployed on Railway
- [ ] Backend URL copied
- [ ] Frontend deployed on Railway
- [ ] `public/config.js` updated with backend URL
- [ ] Code pushed to GitHub
- [ ] Backend health check responds: `https://backend-url/health`
- [ ] Frontend loads in browser
- [ ] Upload test images and verify comparison works

---

## 🆘 Troubleshooting

### Backend Returns 502/503
- **Cause:** Model still loading
- **Fix:** Wait 2-3 more minutes, refresh browser

### Frontend Says "Failed to Fetch"
- **Cause:** Wrong backend URL in config.js
- **Fix:** Check `public/config.js` has correct backend URL
- **Debug:** Open DevTools (F12) → Network tab → check request URL

### Need to Update Code Later
```bash
# Make changes locally
# Push to GitHub
git push origin main

# Railway auto-detects changes
# Wait 1-2 minutes for auto-redeploy
# No manual intervention needed!
```

---

## 💡 Pro Tips

1. **Monitor Logs**
   - Go to Railway dashboard → Your service → Logs
   - Watch real-time deployment logs

2. **Check Memory Usage**
   - Visit: `https://your-backend-url/health`
   - Shows current memory consumption

3. **Add Custom Domain** (Optional)
   - Railway Settings → Domains → Add Custom Domain
   - Requires domain purchase + DNS setup

4. **Update Procfile for Optimization**
   - Already optimized: 1 worker, 2 threads, 300s timeout
   - Adjust if needed in `Procfile`

---

## 📈 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Startup Time** | 1-2 min | Model loading |
| **Request Latency** | 2-5 sec | Per comparison |
| **Memory Usage** | ~300MB | Within 512MB limit |
| **Max Concurrent Users** | ~5 | On free tier |
| **Monthly Cost** | ~$1-2 | Using $5 credit |

---

## 🎯 Common Scenarios

### **Scenario 1: First Time Deployment**
1. Push code to GitHub
2. Go to railway.app
3. Create new project from GitHub
4. Railway does everything automatically
5. Get URLs and update config.js
6. Done! ✅

### **Scenario 2: Making Code Changes**
1. Edit files locally
2. `git push origin main`
3. Railway auto-redeploys (1-2 min)
4. Refresh browser to see changes
5. Done! ✅

### **Scenario 3: More Traffic Needed**
1. Free tier can handle ~5-10 concurrent users
2. If more needed, upgrade Railway plan ($7+/month)
3. Get more RAM and CPU
4. Auto-redeploys with new resources
5. Done! ✅

---

## 📞 Need Help?

- **Railway Docs:** https://docs.railway.app
- **Railway Status:** https://status.railway.app
- **Your Backend Health:** `https://your-backend-url/health`

---

**Last Updated:** November 18, 2025  
**Status:** Ready for Production ✅
