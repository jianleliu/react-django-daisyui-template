#!/bin/bash

# Create a Python virtual environment
python3 -m venv .pyvenv

# Activate the Python virtual environment
source .pyvenv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Create a Node.js environment
# Ensure nodeenv is installed: pip install nodeenv
nodeenv .jsvenv

# Activate Node.js environment and install Node.js dependencies
source .jsvenv/bin/activate
npm install

# Optional: Display a message indicating setup is complete
echo "Setup complete. Python and Node.js environments are set up, and dependencies are installed."
