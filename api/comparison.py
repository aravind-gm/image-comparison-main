# /backend/comparison.py

import numpy as np
from scipy.spatial.distance import cosine
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