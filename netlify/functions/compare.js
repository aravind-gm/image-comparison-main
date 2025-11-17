// Netlify serverless function to proxy API calls
// This allows us to use environment variables

exports.handler = async (event, context) => {
  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  const BACKEND_URL = process.env.BACKEND_URL || 'https://neuralvision-ai.onrender.com/api/compare';

  try {
    // Forward the request to the actual backend
    const response = await fetch(BACKEND_URL, {
      method: 'POST',
      body: event.body,
      headers: {
        'Content-Type': event.headers['content-type']
      }
    });

    const data = await response.json();

    return {
      statusCode: response.status,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
