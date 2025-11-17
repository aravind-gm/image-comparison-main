# /backend/model.py

import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import io

# Define the image transformations required by the pre-trained model (ResNet)
# All pre-trained models on ImageNet expect this normalization and size (224x224)
TRANSFORM = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_feature_extractor():
    """Loads a pre-trained PyTorch model (ResNet-50) and cuts off the final layer."""
    
    # Use torch.hub to load ResNet-50 with best available weights
    try:
        model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
    except AttributeError:
        # Fallback for older torch versions
        model = models.resnet50(pretrained=True)
    
    # Chop off the last fully-connected layer (which is for classification)
    # We only want the output of the average pooling layer (2048-dim vector)
    model = torch.nn.Sequential(*(list(model.children())[:-1]))
    
    # Set the model to evaluation mode (turns off dropout, batch-norm updates, etc.)
    model.eval()
    return model

def get_image_embedding(model, image_input):
    """
    Generates a 2048-dimensional feature vector for a single image.
    
    :param model: The PyTorch feature extractor model.
    :param image_input: An image path string or a file-like object (for uploads).
    :return: A 1D numpy array (the image embedding).
    """
    if isinstance(image_input, str):
        # Input is a file path
        img = Image.open(image_input).convert('RGB')
    else:
        # Input is a file-like object (e.g., from Flask request.files)
        img = Image.open(io.BytesIO(image_input.read())).convert('RGB')
    
    # Apply transformations and add a 'batch' dimension (1, 3, 224, 224)
    img_tensor = TRANSFORM(img).unsqueeze(0)
    
    with torch.no_grad():
        # Get model output (embedding)
        embedding_tensor = model(img_tensor)
        
    # Squeeze to remove extra dimensions and convert to a 1D numpy array
    embedding_array = embedding_tensor.squeeze().cpu().numpy()
    
    return embedding_array