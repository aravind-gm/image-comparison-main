# /backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
try:
    # When running as a module (gunicorn api.app:app)
    from api.comparison import compare_images
except ImportError:
    # When running directly (python api/app.py)
    from comparison import compare_images
import os

# --- Configuration ---
app = Flask(__name__)
CORS(app) 

# --- API Endpoint for Comparison ---

@app.route('/api/compare', methods=['POST'])
def compare_two_images():
    """
    Handles two image uploads, sends them to the comparison logic, 
    and returns a single similarity score.
    """
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
    # NOTE: Run this first before testing the frontend
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, load_dotenv=False)