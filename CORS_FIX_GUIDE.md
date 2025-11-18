# CORS Error Fix Guide

## Problem Description
```
Access to fetch at 'https://neuralvision-ai.onrender.com/api/compare' from origin 'https://neuralvison.netlify.app' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

This error occurs when your frontend (deployed on Netlify) tries to communicate with your backend (deployed on Render), but the backend doesn't properly send CORS (Cross-Origin Resource Sharing) headers.

---

## Root Causes

1. **Flask CORS not configured properly** - Manual header handling wasn't sufficient
2. **Flask-CORS library not installed** - Needed for robust CORS handling
3. **OPTIONS preflight requests failing** - Browser sends preflight checks that must return proper CORS headers

---

## Solution Applied

### Step 1: Install Flask-CORS
Added `Flask-CORS` to `requirements.txt`:
```txt
Flask-CORS
```

### Step 2: Update Backend (api/app.py)
Replaced manual CORS header handling with Flask-CORS initialization:

**Before:**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response
```

**After:**
```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes with explicit configuration
CORS(app, 
     resources={r"/*": {
         "origins": "*",
         "methods": ["GET", "POST", "OPTIONS", "PUT", "DELETE"],
         "allow_headers": ["Content-Type", "Authorization"],
         "expose_headers": ["Content-Type"],
         "max_age": 3600,
         "supports_credentials": False
     }}
)

# Additional CORS headers for extra compatibility
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response
```

### Step 3: Simplify OPTIONS Handler
The OPTIONS preflight handler now just returns a 204 status:
```python
if request.method == 'OPTIONS':
    return '', 204
```

Flask-CORS automatically adds headers to the response.

---

## Deployment Steps

### 1. Update Requirements on Render
The `requirements.txt` has been updated with `Flask-CORS`. When you redeploy to Render:

```bash
# Your deployment command (Render will run this automatically)
pip install -r requirements.txt
gunicorn api.app:app
```

### 2. Redeploy to Render
- Go to your Render dashboard
- Navigate to your service
- Click "Manual Deploy" or push new changes to trigger auto-deployment
- Wait for the deployment to complete

### 3. Verify the Fix
Test the connection:
```bash
# Open browser console and run:
fetch('https://neuralvision-ai.onrender.com/api/compare', {
    method: 'OPTIONS'
}).then(r => console.log('CORS OK:', r.ok)).catch(e => console.error('Error:', e))
```

Expected response headers:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
Access-Control-Allow-Headers: Content-Type,Authorization
Access-Control-Max-Age: 3600
```

---

## How CORS Works

1. **Browser sends preflight OPTIONS request** to check if cross-origin request is allowed
2. **Backend responds with CORS headers** indicating what's allowed
3. **Browser checks response headers**:
   - ✅ If `Access-Control-Allow-Origin: *` → Request allowed
   - ❌ If header missing → CORS error

4. **Actual request sent** if preflight passes
5. **Backend processes request** and includes CORS headers in response

---

## Key CORS Headers Explained

| Header | Purpose |
|--------|---------|
| `Access-Control-Allow-Origin: *` | Allow requests from any origin |
| `Access-Control-Allow-Methods` | Which HTTP methods are allowed (GET, POST, etc.) |
| `Access-Control-Allow-Headers` | Which request headers are allowed |
| `Access-Control-Max-Age` | How long browser can cache preflight response |

---

## Testing Locally

For local development testing:

**Start Backend:**
```bash
python api/app.py
```

**From Frontend (public/index.html):**
```javascript
const API_ENDPOINT = 'http://127.0.0.1:5000/api/compare';
```

The backend CORS config allows all origins, so local requests work without issues.

---

## Troubleshooting

### Still Getting CORS Error?

1. **Clear browser cache:**
   - Press `Ctrl+Shift+Delete` (Windows) or `Cmd+Shift+Delete` (Mac)
   - Clear cookies and cached images/files

2. **Hard refresh:**
   - Press `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)

3. **Check Network Tab:**
   - Open DevTools → Network tab
   - Look for the failed request
   - Click on it and check "Response Headers"
   - Verify `Access-Control-Allow-Origin` is present

4. **Check Render Logs:**
   - Go to Render dashboard → Your service
   - Click on "Logs" tab
   - Look for any Python errors in the logs

5. **Verify Deployment:**
   - Make sure requirements.txt has `Flask-CORS`
   - Make sure `api/app.py` imports `CORS`
   - Trigger manual redeploy on Render

### 502 Bad Gateway Error?

This usually means:
- Backend crashed during deployment
- Python dependencies not installed
- Port not properly exposed

Check Render logs and ensure:
```bash
pip install -r requirements.txt  # All deps installed
gunicorn api.app:app              # Correct start command
```

### Connection Timeout?

- Verify Render service is running (check dashboard status)
- Check if Render free tier has hit resource limits
- Consider upgrading to paid tier if under heavy load

---

## Additional Security Notes

Current setup uses `"origins": "*"` for development ease. For production:

```python
CORS(app, 
     resources={r"/*": {
         "origins": ["https://neuralvison.netlify.app", "https://yourdomain.com"],
         "methods": ["GET", "POST", "OPTIONS"],
         "allow_headers": ["Content-Type"],
         "expose_headers": ["Content-Type"]
     }}
)
```

Replace with your actual domains.

---

## Files Modified

1. ✅ `requirements.txt` - Added `Flask-CORS`
2. ✅ `api/app.py` - Updated CORS configuration with Flask-CORS

---

## Summary

The CORS fix implements industry-standard practices using Flask-CORS library, ensuring:
- ✅ Proper preflight request handling
- ✅ Correct CORS headers on all responses
- ✅ Browser compatibility
- ✅ Cross-domain requests from Netlify to Render work correctly

After deployment, your frontend and backend can communicate without CORS errors.
