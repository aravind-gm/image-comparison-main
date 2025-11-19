# /backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from comparison import compare_images_binary

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    """
    Root endpoint - API health check (lightweight, doesn't load model)
    """
    try:
        import psutil
        memory_info = psutil.Process().memory_info()
        memory_mb = round(memory_info.rss / 1024 / 1024, 2)
    except:
        memory_mb = "N/A"
    
    return jsonify({
        "status": "running",
        "message": "NeuralVision AI Backend API",
        "version": "1.0.1",
        "model": "MobileNetV2",
        "memory_mb": memory_mb,
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
            "model_loaded": compare_images_binary is not None
        }), 200
    except Exception as e:
        return jsonify({
            "status": "degraded",
            "error": str(e)
        }), 500

@app.route('/api/compare', methods=['POST'])
def compare():
    """
    Handles two image uploads, sends them to the comparison logic, 
    and returns a single similarity score.
    """
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"error": "Missing images"}), 400
    
    try:
        result = compare_images_binary(
            request.files['image1'], 
            request.files['image2']
        )
        return jsonify({"match": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("Starting Flask server for Two-Image Comparison...")
    print(f"Python version: {sys.version}")
    print(f"Flask CORS enabled for all origins")
    # NOTE: Run this first before testing the frontend
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, load_dotenv=False)