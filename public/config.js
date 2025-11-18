// Configuration file for NeuralVision AI
// Update the BACKEND_URL when deploying to different environments

const CONFIG = {
    // 🚀 IMPORTANT: Update this URL after deploying to Railway
    // Replace 'your-backend-url' with your actual Railway backend URL
    // Example: 'https://neuralvision-ai-production.up.railway.app/api/compare'
    // 
    // How to find your backend URL:
    // 1. Go to https://railway.app/dashboard
    // 2. Click on your backend service
    // 3. Go to "Domains" section on the right
    // 4. Copy the URL and add '/api/compare' at the end
    //
    BACKEND_URL: 'https://your-backend-url.up.railway.app/api/compare',
    
    // For local development, uncomment this:
    // BACKEND_URL: 'http://127.0.0.1:5000/api/compare',
    
    // API timeout in milliseconds
    API_TIMEOUT: 30000,
    
    // Maximum file size in bytes (10MB)
    MAX_FILE_SIZE: 10 * 1024 * 1024,
};
