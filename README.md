# 🚀 NeuralVision AI - Image Similarity Analyzer

A modern, futuristic web application that uses deep learning (ResNet-50) to compare image similarity.

![NeuralVision AI](https://img.shields.io/badge/AI-Deep%20Learning-purple)
![Python](https://img.shields.io/badge/Python-Flask-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-ResNet--50-red)

---

## 👥 Development Team

**Team Lead:** Aravind GM

**Team Members:**
- Farha Nazz
- Manayatha
- Rithick
- Pranav Jain

---

## ✨ Features

- 🧠 **Deep Learning** - ResNet-50 neural network for feature extraction
- 📊 **Cosine Similarity** - Advanced algorithm for image comparison
- 🎨 **Modern UI** - Futuristic design with particle animations
- 🖱️ **Drag & Drop** - Easy image upload interface
- 📈 **Real-time Analysis** - Instant similarity scoring
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

---

## 🚀 Quick Start (Easy Method)

### For Local Use (Your Computer)

#### Step 1: Install Dependencies (First Time Only)
Double-click on:
```
INSTALL.bat
```

#### Step 2: Run the Application
Double-click on:
```
START_APP.bat
```

That's it! The application will:
- ✅ Start the backend Flask server
- ✅ Open the frontend in your browser
- ✅ Be ready to use!

### For Cloud Deployment (Internet Access)

#### Deploy to Vercel (Easiest)
Double-click on:
```
DEPLOY_TO_VERCEL.bat
```

Or see **CLOUD_DEPLOYMENT.md** for detailed instructions.

Your app will be live at: `https://your-app.vercel.app`

---

## 📂 Project Structure

```
image-comparison-main/
│
├── api/                        # Backend API
│   ├── app.py                 # Flask application
│   ├── comparison.py          # Image comparison logic
│   └── model.py               # ResNet-50 model
│
├── public/                    # Frontend
│   ├── index.html            # Main HTML page
│   └── style.css             # Styling
│
├── requirements.txt          # Python dependencies
├── START_APP.bat            # Main launcher (USE THIS!)
├── INSTALL.bat              # Dependency installer
├── start_backend.bat        # Backend only
└── start_frontend.bat       # Frontend only
```

---

## 🛠️ Manual Setup (Alternative)

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Start Backend:**
```bash
python api/app.py
```

3. **Open Frontend:**
- Open `public/index.html` in your browser

---

## 💻 Technology Stack

### Backend
- **Flask** - Web framework
- **PyTorch** - Deep learning framework
- **torchvision** - Pre-trained models
- **Pillow** - Image processing
- **NumPy** - Numerical computing
- **SciPy** - Scientific computing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with animations
- **JavaScript** - Interactive functionality
- **Canvas API** - Particle animations

### AI/ML
- **ResNet-50** - Pre-trained CNN model
- **Cosine Similarity** - Distance metric
- **2048D Feature Vectors** - Image embeddings

---

## 📖 How to Use

1. **Launch the app** using `START_APP.bat`

2. **Upload Images:**
   - Click "Load Source Image" or drag & drop
   - Click "Load Target Image" or drag & drop

3. **Analyze:**
   - Click "Analyze Similarity" button

4. **View Results:**
   - See similarity score (0-100%)
   - Color-coded interpretation:
     - 🟢 Green: Nearly Identical (>90%)
     - 🔵 Blue: Very Similar (75-90%)
     - 🟡 Yellow: Moderately Similar (50-75%)
     - 🟠 Orange: Somewhat Similar (30-50%)
     - 🔴 Red: Very Different (<30%)

---

## 🎯 API Endpoints

### POST `/api/compare`
Compare two images

**Request:**
- Content-Type: `multipart/form-data`
- Body:
  - `image1`: Image file
  - `image2`: Image file

**Response:**
```json
{
  "status": "success",
  "score": 0.8542,
  "message": "Images successfully compared."
}
```

---

## 🔧 Configuration

### Backend Port
Default: `http://127.0.0.1:5000`

To change, edit `api/app.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=False)
```

### Frontend API Endpoint
Edit `public/index.html`:
```javascript
const API_ENDPOINT = 'http://127.0.0.1:5000/api/compare';
```

---

## 📝 Requirements

```txt
Flask
flask-cors
torch
torchvision
numpy
scipy
Pillow
opencv-python
gunicorn
```

---

## 🐛 Troubleshooting

### Backend won't start
- Ensure Python is installed: `python --version`
- Install dependencies: Run `INSTALL.bat`
- Check if port 5000 is available

### Frontend can't connect to backend
- Make sure backend is running
- Check browser console for errors
- Verify API endpoint URL

### Images won't upload
- Check file format (PNG, JPG supported)
- Ensure file size is under 10MB
- Try different browser

---

## 📊 Performance

- **Model Size:** ~100MB (ResNet-50)
- **Processing Time:** 1-3 seconds per comparison
- **Supported Formats:** JPG, PNG, BMP, GIF
- **Max Image Size:** 10MB

---

## 🌟 Features in Detail

### Particle Animation
- 80 interconnected particles
- Dynamic connections based on distance
- Smooth floating animation

### Glass Morphism UI
- Translucent cards with backdrop blur
- Gradient borders
- Hover effects and animations

### Responsive Design
- Desktop: Full feature layout
- Tablet: Optimized grid
- Mobile: Stacked layout

---

## 📜 License

This project is created by the NeuralVision AI team for educational purposes.

---

## 🙏 Acknowledgments

- PyTorch team for ResNet-50 model
- Flask community
- Open source contributors

---

## 📞 Support

For issues or questions, contact the development team:
- **Team Lead:** Aravind GM

---

**© 2025 NeuralVision AI | All Rights Reserved**

Developed with ❤️ by Aravind GM, Farha Nazz, Manayatha, Rithick, and Pranav Jain
