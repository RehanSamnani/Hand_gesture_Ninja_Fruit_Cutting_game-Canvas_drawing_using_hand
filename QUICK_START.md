# 🚀 Quick Start Guide

Get the Hand Gesture App running in under 5 minutes!

## Prerequisites
- **Python 3.8+** installed
- **Webcam** connected and working
- **Windows, macOS, or Linux**

---

## ⚡ Installation (Choose One)

### 🪟 Windows Users
```bash
# Double-click setup.bat
# OR run in PowerShell:
setup.bat
```

### 🍎 macOS / 🐧 Linux Users
```bash
python setup.py
```

### Manual Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the Game

```bash
python "Ninja Fruit with hand gesture.py"
```

**First run will take 2-3 seconds** to initialize hand detection models.

---

## 🎮 How to Play

### Main Menu
- Press **1** → Ninja Fruit Game 🎯
- Press **2** → Drawing Mode 🎨
- Press **Q** → Quit

---

### Game Mode 1: Ninja Fruit Game 🎯

#### Controls
- 👋 **Move your hand** → Move cursor
- ✋ **Touch fruits** → Cut them (earn 100 points each)
- **M** → Return to Menu
- **Q** → Quit game

#### Gameplay
- Start with **15 lives**
- **Miss a fruit** → Lose 1 life
- **Difficulty increases** every 1000 points
- **Game Over** when lives reach 0

#### Features
- ✨ Fruit cutting animations with particles and "CUT!" text
- 📊 Real-time score, lives, level, and FPS display
- 🎵 Dynamic difficulty progression
- 🌈 Color-coded fruits

---

### Game Mode 2: Drawing Mode 🎨

#### Gestures
- **Open hand** (spread fingers) → Move cursor around
- **Pinch** (thumb touching index) → Draw with brush
- Release pinch to stop drawing

#### Drawing Modes
| Key | Mode | How to Use |
|-----|------|-----------|
| **L** | Line | Pinch, drag to endpoint, release |
| **O** | Circle | Pinch as center, drag to set radius, release |
| **F** | Free | Pinch and draw freehand continuously |

#### Colors (Press Key)
- **R** → Red
- **G** → Green  
- **B** → Blue
- **Y** → Yellow

#### Other Controls
| Key | Action |
|-----|--------|
| **C** | Clear entire canvas |
| **H** | Show/Hide instructions |
| **M** | Return to Menu |
| **Q** | Quit game |

---

## 📸 Tips for Best Results

### Hand Detection
✅ **Good Lighting** - Bright, well-lit environment
✅ **Clear Hands** - Keep hands visible and unobstructed
✅ **Distance** - Position hand 1-2 feet from camera
✅ **Single Hand** - App works best with one hand at a time

### Fruit Game
✅ **Quick Swipes** - Fast hand movements to catch fruits
✅ **Center Position** - Stay in middle of screen for best detection
✅ **Steady Hand** - Smooth, controlled movements work best

### Drawing Mode
✅ **Pinch Clearly** - Make sure thumb and index touch
✅ **Smooth Motions** - Draw slowly for cleaner lines
✅ **Bright Background** - Dark backdrop helps hand detection

---

## 🐛 Troubleshooting

### Camera Not Working
```bash
# Windows - Test camera access
# Settings > Privacy > Camera > Allowed apps
# Give permission to Python

# macOS - Grant camera permission
# System Preferences > Security & Privacy > Camera
```

### Slow Performance
- Close other applications
- Ensure good lighting
- Check internet connection (not needed after setup)
- Reduce screen resolution if needed

### Gestures Not Detected
- Ensure hand is clearly visible
- Increase lighting
- Keep hand within screen bounds
- Remove rings or hand accessories

### ModuleNotFoundError
```bash
# Activate virtual environment first:
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Then verify installation
python -c "import cv2, mediapipe, numpy; print('✓ OK')"
```

---

## 📁 Project Structure

```
Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv/
├── Ninja Fruit with hand gesture.py    # Main game file
├── requirements.txt                     # Python dependencies
├── setup.py                            # Cross-platform setup script
├── setup.bat                           # Windows quick setup
├── README.md                           # Full documentation
├── QUICK_START.md                      # This file
└── hand_landmarker.task                # MediaPipe hand model
```

---

## ❓ FAQ

**Q: Do I need a special camera?**
A: No, any USB webcam or built-in camera works!

**Q: Can I play on Mac/Linux?**
A: Yes! The game runs on all operating systems.

**Q: Is internet needed to play?**
A: Only during initial setup to download dependencies. Offline play after that!

**Q: Why is the virtual environment needed?**
A: It isolates project dependencies from your system Python, preventing conflicts.

**Q: Can I use this on a Raspberry Pi?**
A: You'd need to compile OpenCV for ARM, which is complex. Desktop/laptop recommended.

---

## 🎓 Learn More

- **Full Documentation**: See [README.md](README.md)
- **Project Details**: See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **Technical Questions**: See [VIVA_QUESTIONS.md](VIVA_QUESTIONS.md)

---

## 🆘 Need Help?

1. Check the **Troubleshooting** section above
2. Review **System Requirements** in README.md
3. Ensure camera permissions are granted
4. Try the manual setup option
5. Check Python version: `python --version` (should be 3.8+)

---

**Happy Gaming! 🎮** 

Have fun cutting fruits and drawing! Feel free to share your scores and drawings! 🎨✨
