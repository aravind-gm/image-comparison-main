// server.js - Simple static file server for Railway
// This serves your frontend (public/) as a Node.js service on Railway

const express = require('express');
const path = require('path');
const app = express();

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html for all routes (single-page app support)
// This allows routing within your frontend app
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`✅ Frontend server running on port ${PORT}`);
    console.log(`📱 Public files being served from ./public/`);
});
