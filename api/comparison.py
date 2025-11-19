# /backend/comparison.py

import cv2
import numpy as np
from scipy.spatial.distance import cosine
from skimage.metrics import structural_similarity as ssim
from PIL import Image
try:
    # When running as a module (gunicorn api.app:app)
    from api.model import load_feature_extractor, get_image_embedding
except ImportError:
    # When running directly (python api/app.py)
    from model import load_feature_extractor, get_image_embedding
import io

# Load the feature extractor model only once when the server starts
FEATURE_EXTRACTOR = load_feature_extractor()

def compare_images(image1_file, image2_file):
    """
    Compares two image file-like objects and returns a similarity score.
    
    :param image1_file: A file-like object (Flask upload) for Image 1.
    :param image2_file: A file-like object (Flask upload) for Image 2.
    :return: A similarity score (float between 0.0 and 1.0).
    """
    
    try:
        # 1. Get embeddings for both images
        # NOTE: Your get_image_embedding must be able to handle file-like objects (which it does)
        vector1 = get_image_embedding(FEATURE_EXTRACTOR, image1_file)
        vector2 = get_image_embedding(FEATURE_EXTRACTOR, image2_file)

        # 2. Calculate Cosine Distance
        # Cosine distance ranges from 0 (identical) to 1 (opposite)
        # Cosine Distance = 1 - Cosine Similarity
        cosine_distance = cosine(vector1, vector2)

        # 3. Convert to Similarity Score
        # We invert the distance to get a Similarity Score from 0.0 (least similar) to 1.0 (most similar)
        similarity_score = 1 - cosine_distance

        return similarity_score

    except Exception as e:
        print(f"Error during image comparison: {e}")
        raise

def compare_images_binary(image1_file, image2_file, threshold=0.85):
    """
    Returns 1 (match) or 0 (no match) based on three algorithms.
    """
    # Convert uploads to OpenCV format
    img1 = file_to_cv2(image1_file)
    img2 = file_to_cv2(image2_file)
    
    # Resize both to same size for comparison
    img1 = cv2.resize(img1, (256, 256))
    img2 = cv2.resize(img2, (256, 256))
    
    # Algorithm 1: Histogram Comparison
    hist_score = compare_histograms(img1, img2)
    
    # Algorithm 2: Structural Similarity (SSIM)
    ssim_score = compare_ssim(img1, img2)
    
    # Algorithm 3: ORB Feature Matching
    orb_score = compare_orb_features(img1, img2)
    
    # Average all three scores
    avg_score = (hist_score + ssim_score + orb_score) / 3.0
    
    # Binary decision
    return 1 if avg_score >= threshold else 0

def file_to_cv2(file_obj):
    """Convert Flask upload to OpenCV image"""
    img_bytes = file_obj.read()
    img_pil = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def compare_histograms(img1, img2):
    """Histogram comparison (0-1 score)"""
    hist1 = cv2.calcHist([img1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([img2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist1, hist1)
    cv2.normalize(hist2, hist2)
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def compare_ssim(img1, img2):
    """Structural similarity (0-1 score)"""
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray1, gray2, full=True)
    return max(0, score)  # SSIM can be negative, clamp to 0

def compare_orb_features(img1, img2):
    """ORB feature matching (0-1 score)"""
    orb = cv2.ORB_create(nfeatures=500)
    kp1, des1 = orb.detectAndCompute(cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), None)
    kp2, des2 = orb.detectAndCompute(cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY), None)
    
    if des1 is None or des2 is None:
        return 0.0
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    
    if len(matches) == 0:
        return 0.0
    
    # Ratio of good matches
    return min(1.0, len(matches) / 100)