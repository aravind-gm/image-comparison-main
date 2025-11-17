# ☁️ Cloud Deployment Guide - NeuralVision AI

## 🌐 Vercel Deployment (Easiest for Python/Flask)

### Prerequisites
1. ✅ Node.js installed (for Vercel CLI)
2. ✅ Vercel account (free) - Sign up at https://vercel.com

---

## Option 1: Using DEPLOY_TO_VERCEL.bat (Windows)

### Steps:
1. **Install Node.js** (if not installed)
   - Download from: https://nodejs.org/
   - Install with default settings

2. **Run the deployment script**
   ```
   Double-click: DEPLOY_TO_VERCEL.bat
   ```

3. **Follow the prompts:**
   - Login to Vercel (browser opens)
   - Confirm deployment settings
   - Wait for deployment to complete

4. **Get your URL!**
   - You'll receive a public URL like: `https://your-app.vercel.app`
   - Share this URL with anyone!

---

## Option 2: Manual Deployment (All Platforms)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Navigate to your project
```bash
cd c:\Users\selvi\Downloads\image-comparison-main
```

### Step 4: Deploy
```bash
vercel --prod
```

### Step 5: Done!
Your app is live! Vercel will provide a URL.

---

## Option 3: GitHub + Vercel (Automatic Deployment)

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository (e.g., "neuralvision-ai")

### Step 2: Push Your Code
```bash
cd c:\Users\selvi\Downloads\image-comparison-main
git init
git add .
git commit -m "Initial commit - NeuralVision AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/neuralvision-ai.git
git push -u origin main
```

### Step 3: Connect to Vercel
1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Import your GitHub repository
4. Click "Deploy"

### Step 4: Automatic Updates
- Every time you push to GitHub, Vercel auto-deploys!

---

## 🔧 Configuration Files (Already Set Up!)

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/app.py"
    },
    {
      "src": "/(.*)",
      "dest": "/public/$1"
    }
  ]
}
```
✅ **This is already in your project!**

---

## 📝 Important Notes for Vercel Deployment

### 1. **Environment Variables**
If you need to set any secrets:
```bash
vercel env add MY_SECRET
```

### 2. **Cold Starts**
- First request may be slow (model loading)
- Subsequent requests are faster

### 3. **File Size Limits**
- Vercel has a 50MB deployment limit
- Your app should be fine (PyTorch loads from cache)

### 4. **Function Timeout**
- Free plan: 10 seconds
- May need to upgrade for complex images

---

## 🌍 Alternative Cloud Platforms

### Heroku
```bash
# Install Heroku CLI
# Create Procfile:
web: gunicorn api.app:app
```

### Railway
1. Go to https://railway.app
2. Connect GitHub repo
3. Deploy automatically

### PythonAnywhere
1. Upload files to https://www.pythonanywhere.com
2. Configure WSGI
3. Done!

### AWS / Google Cloud / Azure
- More complex but more control
- See respective documentation

---

## ⚠️ What Changes for Cloud Deployment

### Local (START_APP.bat):
- ✅ Runs on your computer
- ✅ Fast (no internet latency)
- ✅ Free
- ❌ Only you can access
- ❌ Computer must be on

### Cloud (Vercel):
- ✅ Accessible anywhere
- ✅ Share with anyone
- ✅ Always online
- ✅ Professional URL
- ⚠️ Slight latency
- ⚠️ Cold starts

---

## 🔐 Security for Cloud Deployment

### Recommended:
1. **Add Rate Limiting**
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, default_limits=["100 per hour"])
   ```

2. **Add File Size Validation**
   ```python
   MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
   ```

3. **Add Authentication (Optional)**
   - API keys
   - OAuth
   - User accounts

---

## 💰 Cost Comparison

### Vercel
- **Free Tier:** 100GB bandwidth/month
- **Pro:** $20/month for more

### Heroku
- **Free:** 550 hours/month
- **Hobby:** $7/month

### Railway
- **Free:** $5 credit/month
- **Pay as you go**

### PythonAnywhere
- **Free:** Limited (good for testing)
- **Hacker:** $5/month

---

## 📊 Deployment Checklist

Before deploying:
- [ ] Code works locally (START_APP.bat)
- [ ] All dependencies in requirements.txt
- [ ] vercel.json configured (already done!)
- [ ] No sensitive data in code
- [ ] Test with different images
- [ ] Mobile responsive (already done!)

After deploying:
- [ ] Test live URL
- [ ] Check loading times
- [ ] Test image uploads
- [ ] Test on mobile
- [ ] Share URL with team

---

## 🚀 Quick Deployment Command

```bash
# One command deployment:
npx vercel --prod
```

---

## 🐛 Troubleshooting Cloud Deployment

### "Build failed"
- Check requirements.txt
- Ensure Python version compatible
- Check logs: `vercel logs`

### "Function timeout"
- Upgrade Vercel plan
- Optimize model loading
- Use smaller images

### "Module not found"
- Add missing package to requirements.txt
- Redeploy

### "API not responding"
- Check vercel.json routes
- Verify API endpoint in frontend
- Check function logs

---

## 📱 Updating Your Deployed App

### Method 1: Redeploy
```bash
vercel --prod
```

### Method 2: GitHub (if connected)
```bash
git add .
git commit -m "Update"
git push
# Auto-deploys!
```

---

## 🌟 After Deployment

### Share Your App:
```
https://neuralvision-ai.vercel.app
```

### Custom Domain (Optional):
1. Buy domain (namecheap, godaddy)
2. Add to Vercel
3. Configure DNS
4. Use: `https://yourapp.com`

---

## 📞 Support

**For Deployment Issues:**
1. Check Vercel docs: https://vercel.com/docs
2. Check deployment logs
3. Contact team lead: Aravind GM

**For App Issues:**
1. Test locally first (START_APP.bat)
2. Check browser console (F12)
3. Review DEPLOYMENT_GUIDE.md

---

## ✅ Summary

### Local Development:
```
START_APP.bat  ← Use this for development
```

### Cloud Deployment:
```
DEPLOY_TO_VERCEL.bat  ← Use this for cloud
```

### Both are needed for different purposes!

---

**© 2025 NeuralVision AI**

**Team:** Aravind GM (Lead), Farha Nazz, Manayatha, Rithick, Pranav Jain

**Good luck with your deployment! 🚀**
