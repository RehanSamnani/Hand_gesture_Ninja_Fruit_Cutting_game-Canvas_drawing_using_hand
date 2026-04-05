#!/usr/bin/env python3
"""
Setup script for Hand Gesture Interactive App
Creates virtual environment and installs all dependencies
Works on Windows, macOS, and Linux
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    print("\n" + "="*50)
    print(text)
    print("="*50 + "\n")

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"[*] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=False)
        print(f"[✓] {description} completed successfully\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[✗] ERROR: {description} failed")
        print(f"Error: {e}\n")
        return False

def main():
    print_header("Hand Gesture Interactive App Setup")
    
    # Check Python version
    print(f"[*] Detected Python {sys.version}")
    if sys.version_info < (3, 8):
        print("[✗] ERROR: Python 3.8 or higher is required")
        sys.exit(1)
    print("[✓] Python version OK\n")
    
    # Get OS info
    os_name = platform.system()
    print(f"[*] Detected OS: {os_name}\n")
    
    # Step 1: Create virtual environment
    print_header("Step 1/3: Creating Virtual Environment")
    
    venv_dir = ".venv"
    if os.path.exists(venv_dir):
        print(f"[*] Virtual environment already exists at {venv_dir}")
        response = input("[?] Remove and recreate? (y/n): ").strip().lower()
        if response == 'y':
            import shutil
            shutil.rmtree(venv_dir)
            print(f"[*] Removed {venv_dir}\n")
        else:
            print("[*] Using existing environment\n")
    
    if not os.path.exists(venv_dir):
        if not run_command(f"{sys.executable} -m venv {venv_dir}", 
                          "Creating virtual environment"):
            sys.exit(1)
    
    # Determine activation script path
    if os_name == "Windows":
        activate_script = f"{venv_dir}\\Scripts\\activate.bat"
        python_exe = f"{venv_dir}\\Scripts\\python.exe"
    else:  # macOS / Linux
        activate_script = f"{venv_dir}/bin/activate"
        python_exe = f"{venv_dir}/bin/python3"
    
    # Step 2: Install requirements
    print_header("Step 2/3: Installing Dependencies")
    
    pip_cmd = f"{python_exe} -m pip install --upgrade pip"
    if not run_command(pip_cmd, "Upgrading pip"):
        sys.exit(1)
    
    req_cmd = f"{python_exe} -m pip install -r requirements.txt"
    if not run_command(req_cmd, "Installing requirements from requirements.txt"):
        sys.exit(1)
    
    # Step 3: Verify installation
    print_header("Step 3/3: Verifying Installation")
    
    verify_cmd = f"{python_exe} -c \"import cv2; import mediapipe; import numpy; print('All packages imported successfully')\""
    if not run_command(verify_cmd, "Verifying installations"):
        print("[!] WARNING: Verification failed, but setup may still be functional\n")
    
    # Success message
    print_header("Setup Completed Successfully!")
    
    print("To run the application:\n")
    if os_name == "Windows":
        print("  1. Activate environment:")
        print(f"     {activate_script}\n")
        print("  2. Run the application:")
        print("     python hand_gesture_interactive_app.py\n")
    else:  # macOS / Linux
        print("  1. Activate environment:")
        print(f"     source {activate_script}\n")
        print("  2. Run the application:")
        print("     python hand_gesture_interactive_app.py\n")
    
    print("="*50)
    print("Happy gesture-based drawing and gaming!")
    print("="*50 + "\n")
    
    # Offer to run the app immediately
    response = input("[?] Would you like to run the app now? (y/n): ").strip().lower()
    if response == 'y':
        if os_name == "Windows":
            cmd = f"cmd /c \"{activate_script} && python hand_gesture_interactive_app.py\""
        else:
            cmd = f"bash -c 'source {activate_script} && python hand_gesture_interactive_app.py'"
        
        os.system(cmd)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[✗] Unexpected error: {e}")
        sys.exit(1)
