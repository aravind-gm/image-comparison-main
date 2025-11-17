# 🚀 Deployment Guide - NeuralVision AI

## For End Users (Simple Method)

### First Time Setup

1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Install Dependencies**
   - Double-click `INSTALL.bat`
   - Wait for installation to complete

3. **Run the Application**
   - Double-click `START_APP.bat`
   - Application will start automatically!

---

## Available Scripts

### 📦 `INSTALL.bat`
- Installs all required Python packages
- Run this ONCE before first use

### ▶️ `START_APP.bat` (MAIN LAUNCHER)
- Starts both backend and frontend
- Opens application in browser
- **USE THIS to run the app!**

### 🔧 `start_backend.bat`
- Starts only the Flask backend server
- For development/debugging

### 🌐 `start_frontend.bat`
- Opens only the frontend
- Backend must be running separately

---

## File Structure for Deployment

```
📁 NeuralVision-AI/
│
├── 📄 START_APP.bat          ⭐ MAIN FILE - Run this!
├── 📄 INSTALL.bat            ⭐ Run once to install
├── 📄 README.md              📖 Documentation
├── 📄 requirements.txt       📦 Dependencies
├── 📄 vercel.json            ☁️ Cloud deployment config
│
├── 📁 api/                   🔙 Backend
│   ├── app.py
│   ├── comparison.py
│   └── model.py
│
└── 📁 public/                🎨 Frontend
    ├── index.html
    └── style.css
```

---

## Sharing/Distributing Your Application

### Option 1: ZIP File (Easiest)
1. Right-click the `image-comparison-main` folder
2. Select "Send to → Compressed (zipped) folder"
3. Share the ZIP file
4. Recipients: Extract and run `START_APP.bat`

### Option 2: GitHub
```bash
git init
git add .
git commit -m "NeuralVision AI Application"
git remote add origin <your-repo-url>
git push -u origin main
```

### Option 3: Cloud Deployment (Vercel)
1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

---

## System Requirements

### Minimum
- **OS:** Windows 7/8/10/11
- **Python:** 3.8+
- **RAM:** 4GB
- **Storage:** 500MB free space
- **Internet:** Required for first-time model download

### Recommended
- **OS:** Windows 10/11
- **Python:** 3.9+
- **RAM:** 8GB
- **Storage:** 1GB free space
- **GPU:** Optional (speeds up processing)

---

## Troubleshooting

### "Python is not recognized"
**Solution:** Install Python and add to PATH
- Download: https://www.python.org/downloads/
- During installation, check ✅ "Add Python to PATH"

### "pip is not recognized"
**Solution:** Reinstall Python with pip
- Or manually: `python -m ensurepip --upgrade`

### Port 5000 already in use
**Solution 1:** Close other applications using port 5000
**Solution 2:** Change port in `api/app.py`:
```python
app.run(host='0.0.0.0', port=8000)  # Change to 8000
```
Then update frontend `index.html`:
```javascript
const API_ENDPOINT = 'http://127.0.0.1:8000/api/compare';
```

### Backend starts but frontend can't connect
1. Check if backend is running (window should be open)
2. Check browser console (F12) for errors
3. Verify API endpoint URL matches backend port

### Images won't upload
1. Check file format (JPG, PNG supported)
2. Ensure file size < 10MB
3. Try different browser (Chrome/Edge recommended)

### Slow processing
- First run downloads ResNet-50 model (~100MB)
- Subsequent runs will be faster
- Consider upgrading RAM or using GPU

---

## Network Deployment (LAN Access)

To allow others on your network to access:

1. Find your local IP:
   ```cmd
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Modify `api/app.py`:
   ```python
   app.run(host='0.0.0.0', port=5000)  # Already set!
   ```

3. Share with others:
   ```
   http://YOUR-IP:5000
   ```

4. Update frontend for others:
   - They need to edit `index.html` API_ENDPOINT:
   ```javascript
   const API_ENDPOINT = 'http://192.168.1.100:5000/api/compare';
   ```

---

## Production Deployment

### Using Gunicorn (Linux/Mac)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 api.app:app
```

### Using Vercel (Serverless)
- Already configured via `vercel.json`
- Run: `vercel --prod`

### Using Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "api/app.py"]
```

Build and run:
```bash
docker build -t neuralvision-ai .
docker run -p 5000:5000 neuralvision-ai
```

---

## Performance Optimization

### Speed up model loading
- Model is cached after first download
- Location: `~/.cache/torch/hub/`

### Reduce memory usage
- Close unnecessary applications
- Use smaller images for comparison

### Enable GPU acceleration
- Install CUDA-enabled PyTorch:
  ```bash
  pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
  ```

---

## Security Notes

### For Local Use (Default)
- ✅ Safe - Only accessible from your computer
- Backend: `127.0.0.1:5000` (localhost)

### For Network Use
- ⚠️ Ensure firewall rules are appropriate
- 🔒 Consider adding authentication
- 🚫 Don't expose to public internet without security

---

## Updates & Maintenance

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Checking Python Version
```cmd
python --version
```

### Viewing Installed Packages
```cmd
pip list
```

---

## Support & Contact

**Development Team:**
- **Lead:** Aravind GM
- **Members:** Farha Nazz, Manayatha, Rithick, Pranav Jain

For issues:
1. Check this guide
2. Review README.md
3. Check error messages
4. Contact team lead

---

## Quick Command Reference

```cmd
# Install dependencies
INSTALL.bat

# Run application (MAIN)
START_APP.bat

# Backend only
start_backend.bat

# Frontend only
start_frontend.bat

# Check Python
python --version

# Check pip
pip --version

# Install single package
pip install <package-name>

# View logs
# Check terminal/console output
```

---

## Backup & Safety

### Before Deployment
1. ✅ Test on your machine
2. ✅ Backup original files
3. ✅ Document any changes
4. ✅ Test all features

### Regular Maintenance
- 📅 Update dependencies monthly
- 💾 Backup configuration changes
- 📊 Monitor performance
- 🐛 Fix bugs promptly

---

**© 2025 NeuralVision AI**

**Team:** Aravind GM (Lead), Farha Nazz, Manayatha, Rithick, Pranav Jain

---

## ✅ Final Checklist

- [ ] Python installed
- [ ] Dependencies installed (`INSTALL.bat`)
- [ ] Application runs (`START_APP.bat`)
- [ ] Frontend opens in browser
- [ ] Backend responds
- [ ] Images upload successfully
- [ ] Similarity analysis works
- [ ] Results display correctly

**All checked? You're ready to deploy! 🚀**
