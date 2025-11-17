#!/usr/bin/env python3
"""
NeuralVision AI - Image Comparison App Runner
This script starts both the backend Flask server and opens the frontend in the browser.
"""

import subprocess
import time
import webbrowser
import os
import sys

def main():
    print("=" * 50)
    print("   NeuralVision AI - Starting Application")
    print("=" * 50)
    print()

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the backend script
    backend_script = os.path.join(current_dir, 'api', 'app.py')

    print("[1/2] Starting Backend Flask Server...")
    # Start the backend in a subprocess
    backend_process = subprocess.Popen([sys.executable, backend_script])

    print("✓ Backend server starting on http://127.0.0.1:5000")
    print()

    print("[2/2] Waiting 3 seconds for server to initialize...")
    time.sleep(3)

    print("✓ Opening Frontend...")
    # Path to the frontend HTML file
    frontend_path = os.path.join(current_dir, 'public', 'index.html')
    # Open in browser
    webbrowser.open(f'file://{frontend_path}')

    print()
    print("=" * 50)
    print("✓ Application started successfully!")
    print("=" * 50)
    print()
    print("Backend:  http://127.0.0.1:5000")
    print("Frontend: Opened in your browser")
    print()
    print("Team Lead: Aravind GM")
    print("Team: Farha Nazz, Manayatha, Rithick, Pranav Jain")
    print()
    print("=" * 50)
    print("Press Ctrl+C to stop the application...")
    print("=" * 50)

    try:
        # Wait for the backend process to finish
        backend_process.wait()
    except KeyboardInterrupt:
        print()
        print("Stopping application...")
        backend_process.terminate()
        backend_process.wait()
        print("Application stopped.")

if __name__ == "__main__":
    main()