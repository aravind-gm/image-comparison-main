# 🚀 Alternative Deployment Options for NeuralVision AI

## ⚠️ Why Vercel Won't Work

Vercel's free tier has **8GB RAM limit** during builds. Your app uses:
- PyTorch (~800MB)
- TorchVision (~100MB)
- Other dependencies

The installation process exceeds 8GB RAM, causing **Out of Memory (OOM)** errors.

---

## ✅ Recommended Alternatives

### 1. **Render.com** (FREE - BEST OPTION)

**Pros:**
- ✅ FREE tier available
- ✅ 512MB RAM (enough for Python apps)
- ✅ Supports large dependencies like PyTorch
- ✅ Auto-deploys from GitHub
- ✅ Free SSL certificate
- ✅ Better for ML/AI applications

**How to Deploy:**

1. **Create account:** https://render.com

2. **Push code to GitHub:**
   ```cmd
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

3. **Create Web Service on Render:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name:** `neuralvision-ai`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn api.app:app`
     - **Instance Type:** Free

4. **Update frontend to use Render URL:**
   - You'll get a URL like: `https://neuralvision-ai.onrender.com`
   - Update `public/index.html` API endpoint

---

### 2. **Railway.app** (FREE $5 credit/month)

**Pros:**
- ✅ $5 free credit monthly
- ✅ Good for Python apps
- ✅ Easy deployment
- ✅ Supports PyTorch

**How to Deploy:**

1. **Create account:** https://railway.app

2. **Deploy from GitHub:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure:**
   - Railway auto-detects Python
   - Add start command: `gunicorn api.app:app`
   - Set port: `5000`

---

### 3. **PythonAnywhere** (FREE tier)

**Pros:**
- ✅ Completely FREE
- ✅ Built for Python/Flask
- ✅ No credit card required
- ✅ Easy setup

**Cons:**
- ⚠️ Limited to CPU (no GPU)
- ⚠️ Slower performance

**How to Deploy:**

1. **Create account:** https://www.pythonanywhere.com

2. **Upload files:**
   - Use "Files" tab to upload your code
   - Or clone from GitHub

3. **Setup Web App:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Flask
   - Point to your `api/app.py`

4. **Install dependencies:**
   ```bash
   pip install --user -r requirements.txt
   ```

---

### 4. **Heroku** (NO LONGER FREE)

**Note:** Heroku discontinued free tier in November 2022.
- Costs $7/month minimum
- Good for production apps

---

### 5. **Google Cloud Run** (FREE tier available)

**Pros:**
- ✅ Free tier: 2 million requests/month
- ✅ Scales to zero (no cost when idle)
- ✅ Supports Docker containers

**Setup:**

1. **Create `Dockerfile`:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "api.app:app"]
```

2. **Deploy:**
```cmd
gcloud run deploy neuralvision-ai --source .
```

---

### 6. **AWS EC2 Free Tier** (12 months free)

**Pros:**
- ✅ Full control
- ✅ 750 hours/month free
- ✅ Good for learning

**Cons:**
- ⚠️ More complex setup
- ⚠️ Requires server management

---

### 7. **Netlify** (NOT RECOMMENDED)

**Why not:**
- ❌ Similar to Vercel
- ❌ 256MB memory limit
- ❌ Not suitable for ML/AI apps

---

## 📊 Comparison Table

| Platform | Free Tier | RAM | Best For | Difficulty |
|----------|-----------|-----|----------|------------|
| **Render** | ✅ Yes | 512MB | ML Apps | ⭐⭐ Easy |
| **Railway** | ✅ $5/mo | 1GB+ | Python | ⭐⭐ Easy |
| **PythonAnywhere** | ✅ Yes | Limited | Simple Flask | ⭐ Very Easy |
| **Google Cloud Run** | ✅ Yes | 2GB | Containers | ⭐⭐⭐ Medium |
| **AWS EC2** | ✅ 12mo | 1GB | Full Control | ⭐⭐⭐⭐ Hard |
| **Vercel** | ✅ Yes | 8GB build | Static/Next.js | ❌ OOM Error |
| **Heroku** | ❌ No | - | - | Paid Only |

---

## 🎯 Our Recommendation: Use **Render.com**

### Why Render?
1. ✅ **Completely FREE** forever
2. ✅ **Easy setup** - Deploy in 5 minutes
3. ✅ **GitHub integration** - Auto-deploy on push
4. ✅ **PyTorch compatible** - No OOM errors
5. ✅ **Free SSL** - Automatic HTTPS
6. ✅ **Good performance** for AI/ML apps

---

## 🔧 Quick Setup for Render.com

### Step 1: Prepare Your Code

Add `Procfile` in project root:
```
web: gunicorn api.app:app
```

### Step 2: Push to GitHub
```cmd
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/aravind-gm/image-comparison-main.git
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to https://render.com
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Select your repository
5. Configure:
   - **Name:** neuralvision-ai
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn api.app:app`
6. Click "Create Web Service"

### Step 4: Update Frontend

Your backend will be at: `https://neuralvision-ai.onrender.com`

Update `public/index.html`:
```javascript
const API_ENDPOINT = 'https://neuralvision-ai.onrender.com/api/compare';
```

**Note:** If you encounter import errors, the code has been updated to handle both local and deployed environments automatically.

---

## 🆘 Still Having Issues?

### Option A: Deploy Backend Only
- Deploy backend to Render
- Keep frontend local or on GitHub Pages

### Option B: Reduce Dependencies
- Use smaller models
- Remove unnecessary packages
- Consider lightweight alternatives

### Option C: Use Local Network
- Run on your computer
- Access via LAN (see DEPLOYMENT_GUIDE.md)

---

## 📝 Notes

- **First deployment takes 5-10 minutes** (downloading PyTorch)
- **Subsequent deployments are faster** (cached dependencies)
- **Free tier sleeps after 15 min inactivity** (wakes up in ~30 seconds)
- **Upgrade to paid plan** for 24/7 uptime ($7/month)

---

**Ready to deploy? Start with Render.com! 🚀**

*Team: Aravind GM (Lead), Farha Nazz, Manayatha, Rithick, Pranav Jain*
