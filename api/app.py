# /backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
try:
    # When running as a module (gunicorn api.app:app)
    from api.comparison import compare_images
except ImportError:
    # When running directly (python api/app.py)
    from comparison import compare_images
except Exception as e:
    print(f"Error importing comparison module: {e}")
    compare_images = None
import os
import sys

# --- Configuration ---
app = Flask(__name__)
# Enable CORS for all origins (allows Netlify, local, and other frontends to access the API)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}}, supports_credentials=False) 

# --- API Endpoints ---

@app.route('/', methods=['GET'])
def home():
    """
    Root endpoint - API health check (lightweight, doesn't load model)
    """
    import psutil
    memory_info = psutil.Process().memory_info()
    return jsonify({
        "status": "running",
        "message": "NeuralVision AI Backend API",
        "version": "1.0.1",
        "model": "MobileNetV2",
        "memory_mb": round(memory_info.rss / 1024 / 1024, 2),
        "endpoints": {
            "/api/compare": "POST - Compare two images",
            "/health": "GET - Detailed health check"
        }
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """
    Detailed health check endpoint
    """
    try:
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()
        return jsonify({
            "status": "healthy",
            "memory": {
                "rss_mb": round(memory_info.rss / 1024 / 1024, 2),
                "vms_mb": round(memory_info.vms / 1024 / 1024, 2)
            },
            "model_loaded": compare_images is not None
        }), 200
    except Exception as e:
        return jsonify({
            "status": "degraded",
            "error": str(e)
        }), 500

@app.route('/api/compare', methods=['POST', 'OPTIONS'])
def compare_two_images():
    """
    Handles two image uploads, sends them to the comparison logic, 
    and returns a single similarity score.
    """
    # Handle preflight OPTIONS request for CORS
    if request.method == 'OPTIONS':
        return '', 204
    # 1. Validate Both Files
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"error": "Missing one or both image files ('image1', 'image2')"}), 400
    
    image1_file = request.files['image1']
    image2_file = request.files['image2']
    
    if image1_file.filename == '' or image2_file.filename == '':
        return jsonify({"error": "One or both file inputs were empty"}), 400

    # 2. Call the core comparison logic
    try:
        # The files are passed as file-like objects to the comparison function
        similarity_score = compare_images(image1_file, image2_file)
        
        # 3. Return the result
        return jsonify({
            "status": "success",
            "score": float(similarity_score),
            "message": f"Images successfully compared."
        }), 200

    except Exception as e:
        print(f"An error occurred during comparison: {e}")
        # Return a 500 status code for internal server errors
        return jsonify({"error": f"Internal processing error: {e}"}), 500


if __name__ == '__main__':
    print("Starting Flask server for Two-Image Comparison...")
    print(f"Python version: {sys.version}")
    print(f"Flask CORS enabled for all origins")
    # NOTE: Run this first before testing the frontend
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, load_dotenv=False)