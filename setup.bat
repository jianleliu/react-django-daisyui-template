@echo off
REM Create a Python virtual environment
python -m venv .pyvenv

REM Activate the Python virtual environment
call .pyvenv\Scripts\activate.bat

REM Install Python dependencies
pip install -r requirements.txt

REM Create a Node.js environment
nodeenv .jsvenv

REM Open a new Command Prompt window and install Node.js dependencies
start cmd /k "cd /d %~dp0 && .jsvenv\Scripts\activate && npm install"

REM Optional: Display a message indicating setup is complete
echo Setup complete. Python and Node.js environments are set up, and dependencies are installed.
