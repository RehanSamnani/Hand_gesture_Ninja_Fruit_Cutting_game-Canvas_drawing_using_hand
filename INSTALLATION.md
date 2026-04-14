# 📦 Installation Guide

Complete installation instructions for all platforms.

## System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 4GB
- **Storage**: 500MB free space
- **Webcam**: Any USB webcam or built-in camera
- **Display**: 1280x720 or higher

### Recommended Requirements
- **Python**: 3.10 or higher
- **RAM**: 8GB or more
- **CPU**: Intel i5/i7 or AMD Ryzen 5/7
- **GPU**: 2GB VRAM (for smooth 60 FPS)
- **Network**: Broadband for initial setup

---

## Platform-Specific Installation

### 🪟 Windows 10/11

#### Method 1: Automatic Setup (Recommended)
```bash
# Navigate to project folder
cd "Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv"

# Run the setup batch file
setup.bat
```

**What it does:**
- Creates Python virtual environment
- Installs all dependencies
- Verifies installation
- Displays success message

#### Method 2: Python Setup Script
```bash
cd "Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv"
python setup.py
```

#### Method 3: Manual Setup
```bash
# Navigate to project directory
cd "Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify (optional)
python -c "import cv2, mediapipe, numpy; print('✓ All packages installed')"
```

---

### 🍎 macOS

#### Prerequisites
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10 or higher
brew install python@3.10
```

#### Setup
```bash
# Navigate to project
cd "Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv"

# Option 1: Python setup script
python3 setup.py

# Option 2: Manual setup
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Grant Camera Permission
```bash
# macOS requires explicit camera permissions
# 1. Go to: System Preferences → Security & Privacy → Camera
# 2. Allow Terminal or Python to access camera
# 3. Restart the application
```

---

### 🐧 Linux (Ubuntu/Debian)

#### Prerequisites
```bash
# Update package manager
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3.10 python3-pip python3-venv

# Install system libraries for OpenCV
sudo apt install -y libatlas-base-dev libjasper-dev libtiff5 libjasper-dev libjasper1 \
  libharfbuzz0b libwebp6 libtiff5 libjasper1 libqtgui4 python3-pyqt5 \
  libatlas-base-dev libjasper-dev libharfbuzz0b libwebp6 libhdf5-dev libharfbuzz0b libwebp6

# Install camera support
sudo apt install -y libv4l-dev
```

#### Setup
```bash
# Clone repository (if using git)
git clone https://github.com/yourusername/Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv.git
cd Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv

# Setup
python3 setup.py

# Or manual setup
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

#### Enable Webcam Access
```bash
# Add user to video group for camera access
sudo usermod -aG video $USER

# Apply changes (may require logout/login)
newgrp video
```

---

### 🐧 Linux on Raspberry Pi

**Note**: Full setup is complex. For Raspberry Pi, consider:
1. Using Raspberry Pi OS with pre-compiled packages
2. Installing from pip wheels designed for ARM
3. Using Docker for easier setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.10+
sudo apt install -y python3.10 python3-pip python3-venv

# Install system libraries
sudo apt install -y libatlas-base-dev libjasper-dev libtiff5 libqtgui4 \
  python3-pyqt5 libharfbuzz0b libwebp6 libv4l-dev

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# Install packages (may take 5-10 minutes)
pip install -r requirements.txt
```

---

## Verification

### Test Installation
```bash
# Activate virtual environment first
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Run test
python -c "import cv2, mediapipe, numpy; print('✓ All imports successful')"
```

### Expected Output
```
✓ All imports successful
```

### Test Camera Access
```bash
# Quick camera test (you may need to grant permissions)
python -c "import cv2; cap = cv2.VideoCapture(0); print('✓ Camera accessible' if cap.isOpened() else '✗ Camera not found')"
```

---

## Upgrading Dependencies

To upgrade to the latest versions:
```bash
# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Upgrade specific packages
pip install --upgrade opencv-python mediapipe numpy
```

---

## Troubleshooting

### Error: Python not found
```bash
# Check Python installation
python --version

# If not found, install Python from python.org
# Windows/macOS: Download from https://python.org
# Linux: sudo apt install python3.10+
```

### Error: Permission denied
```bash
# On Linux/macOS, add execute permission:
chmod +x setup.py
```

### Error: pip: command not found
```bash
# Install pip
python -m ensurepip --upgrade

# Then retry setup
```

### Error: Virtual environment fails
```bash
# Delete existing environment
rm -rf .venv  # Linux/macOS
rmdir /s .venv  # Windows

# Recreate it
python -m venv .venv

# Reactivate and install
```

### Error: Camera not recognized
```bash
# Windows: Check Device Manager → Cameras
# macOS: System Preferences → Security & Privacy → Camera
# Linux: lsusb | grep Camera  or  ls /dev/video*
```

### Error: Out of memory
```bash
# Close other applications
# Reduce screen resolution
# Or upgrade RAM
```

### Error: Module import fails after installation
```bash
# Make sure virtual environment is activated:
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
```

---

## Clean Installation

If you encounter persistent issues:

```bash
# 1. Remove virtual environment
rm -rf .venv  # Linux/macOS
rmdir /s /q .venv  # Windows

# 2. Remove cache
rm -rf __pycache__  # Linux/macOS
rmdir /s /q __pycache__  # Windows

# 3. Start fresh
python -m venv .venv
# Activate venv
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Verify
python -c "import cv2, mediapipe, numpy; print('✓ Success')"
```

---

## Docker Installation (Optional)

For consistent cross-platform setup:

```bash
# Create Dockerfile with contents below
# Then run:
docker build -t hand-gesture-app .
docker run --rm -it --device /dev/video0 hand-gesture-app
```

**Dockerfile contents:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    libv4l-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run app
CMD ["python", "Ninja Fruit with hand gesture.py"]
```

---

## Next Steps

After successful installation:

1. **Quick Start**: See [QUICK_START.md](QUICK_START.md)
2. **Run Game**: `python "Ninja Fruit with hand gesture.py"`
3. **Full Documentation**: See [README.md](README.md)
4. **Troubleshooting**: Return to this guide's troubleshooting section

---

## Support

If installation issues persist:

1. Check **Troubleshooting** section above
2. Verify all **System Requirements**
3. Try **Clean Installation** procedure
4. Check project **Issues** on GitHub
5. Create a new Issue with:
   - Your OS and Python version
   - Error message
   - Steps you took

---

**Happy installing! 🚀**
