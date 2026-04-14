# 🤝 Contributing Guide

Thank you for your interest in contributing to the Hand Gesture Interactive Application! This guide will help you understand how to contribute effectively.

## 🎯 How to Contribute

### Reporting Bugs
Found a bug? Help us fix it!

1. **Check existing issues** - Don't report duplicates
2. **Create a detailed bug report** with:
   - Your OS and Python version
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Error messages or screenshots
   - Your hardware specs (CPU, RAM, Camera)

### Suggesting Features
Have an idea? We'd love to hear it!

1. **Check existing issues/discussions** - Your idea might already be planned
2. **Create a feature request** with:
   - Clear description of the feature
   - Why it would be useful
   - Example use cases
   - Any technical considerations

### Improving Documentation
Documentation improvements are always welcome!

- Fix typos or clarify explanations
- Add examples or use cases
- Improve installation instructions
- Add troubleshooting tips

---

## 💻 Code Contributions

### Setup Development Environment

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv.git
cd Ninja-Fruit-Like-Game-with-hand-gesture-and-opencv

# 3. Add upstream remote
git remote add upstream https://github.com/RehanSamnani/Hand_gesture_Ninja_Fruit_Cutting_game-Canvas_drawing_using_hand.git

# 4. Create feature branch
git checkout -b feature/your-feature-name

# 5. Set up development environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Making Changes

#### Code Style Guidelines

```python
# ✅ DO
def cut_fruit(position, fruit_list):
    """Cut a fruit at the given position.
    
    Args:
        position: (x, y) tuple of cursor position
        fruit_list: List of fruit dictionaries
    
    Returns:
        bool: True if fruit was cut, False otherwise
    """
    for fruit in fruit_list:
        if calculate_distance(position, fruit["position"]) < fruit["radius"]:
            return True
    return False


# ❌ DON'T
def cf(p, f):  # Unclear names
    # This function cuts stuff
    for x in f:
        if abs(p[0] - x[0]) + abs(p[1] - x[1]) < 30:
            return 1
    return 0
```

**Style Requirements:**
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where helpful
- Comment complex logic
- Maximum line length: 100 characters

#### Test Your Changes

```bash
# 1. Verify syntax
python -m py_compile "Ninja Fruit with hand gesture.py"

# 2. Test manually
python "Ninja Fruit with hand gesture.py"

# 3. Test setup script
python setup.py

# 4. Verify requirements
python -c "import cv2, mediapipe, numpy; print('✓ OK')"
```

#### Commit Messages

```
✨ Add fruit cutting animation system

- Add create_fruit_explosion() function for particle effects
- Add draw_fruit_explosions() to render animations  
- Add "CUT!" text feedback at impact point
- Increase animation duration to 0.8 seconds for visibility

Fixes #123
```

**Format:**
- First line: Emoji + short title (50 chars max)
- Blank line
- Detailed explanation (if needed)
- Reference issues: `Fixes #123` or `Related to #456`

**Emojis:**
- ✨ New feature
- 🐛 Bug fix
- 📝 Documentation
- ♻️ Refactoring
- ⚡ Performance
- 🔧 Configuration
- 🎨 UI/UX

### Creating a Pull Request

```bash
# 1. Push your changes
git push origin feature/your-feature-name

# 2. Create PR on GitHub with:
# - Clear title describing change
# - Description explaining what/why
# - Related issues (Fixes #123)
# - Testing evidence (screenshots/videos)
# - Checklist of changes
```

**PR Checklist:**
- [ ] Code follows style guidelines
- [ ] No new warnings introduced
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No unrelated changes
- [ ] Commits well-organized

### Code Review Process

1. **Reviewer assigned** - We'll review your PR
2. **Feedback provided** - Request changes if needed
3. **Updates made** - Address feedback
4. **Approval** - PR approved when ready
5. **Merge** - Your contribution is merged!

---

## 📚 Project Architecture

### Main Components

```
┌─ Input Layer ─────────────┐
│  Camera → Hand Detection   │
└────────────┬──────────────┘
             │
┌────────────▼──────────────┐
│  Gesture Recognition      │ 
│  (Pinch detection, etc)   │
└────────────┬──────────────┘
             │
┌────────────▼──────────────┐
│  Game Logic              │
│  (Scoring, collision)     │
└────────────┬──────────────┘
             │
┌────────────▼──────────────┐
│  Rendering                │
│  (Drawing, UI)            │
└─────────────────────────┘
```

### Key Functions to Know

**Hand Detection:**
- `is_pinching()` - Detect pinch gesture
- `get_hand_position()` - Get cursor position
- `get_thumb_position()` - Get thumb tip position

**Game Logic:**
- `Spawn_Fruits()` - Create new fruit
- `Fruit_Movement()` - Update fruit positions
- `distance()` - Calculate distance (collision)

**Drawing:**
- `create_fruit_explosion()` - Create animation
- `draw_fruit_explosions()` - Render animations
- `draw_drawing_ui()` - Draw interface
- `draw_drawing_instructions()` - Show help

---

## 🎯 Development Ideas

### Easy (Good for beginners)
- [ ] Add sound effects
- [ ] Add more fruit types/colors
- [ ] Improve game instructions
- [ ] Add score persistence (save high scores)
- [ ] Add pause feature

### Medium
- [ ] Add difficulty levels (Easy/Normal/Hard)
- [ ] Multi-hand support (both hands)
- [ ] Add combo system (consecutive cuts)
- [ ] Custom color picker in drawing mode
- [ ] Save/load drawings

### Advanced
- [ ] GPU acceleration for hand detection
- [ ] Multiplayer mode
- [ ] Gesture recognition improvements
- [ ] AI opponent
- [ ] Mobile app version

---

## 🐛 Finding Bugs

To find bugs:

1. **Manual testing** - Play extensively, try edge cases
2. **Stress testing** - Use for long periods
3. **Different environments** - Test on different machines
4. **Different cameras** - Test with various webcams
5. **Low-light conditions** - Test in poor lighting

When you find a bug:
```
1. Document it clearly
2. Create minimal reproduction case
3. Note exact error message
4. Screenshot/record if visual issue
5. Open issue on GitHub
```

---

## 📊 Getting Recognition

Contributors are recognized through:
- Commits logged in git history
- GitHub contributor graph
- [Contributors section in README](README.md) (coming soon!)

---

## 🚀 After Your PR is Merged

Congratulations! Your contribution is now part of the project.

- Update your local repo: `git pull upstream main`
- Delete your feature branch: `git branch -d feature/your-feature`
- Share your contribution!

---

## 📞 Questions?

- Check [README.md](README.md)
- Review [VIVA_QUESTIONS.md](VIVA_QUESTIONS.md)
- Open a GitHub Discussion
- Create an Issue with your question

---

## 📋 Code of Conduct

### Be Respectful
- Treat everyone with respect
- Welcome diverse perspectives
- No harassment or discrimination

### Be Helpful
- Answer questions patiently
- Provide constructive feedback
- Help others learn

### Be Honest
- Give credit for ideas
- Acknowledge limitations
- Admit mistakes

---

## 🎓 Learning Resources

### Computer Vision
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Hands Guide](https://google.github.io/mediapipe/solutions/hands)

### Python
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

### Git
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

---

## 🎉 Thank You!

Your contributions make this project better. We appreciate your effort and enthusiasm!

**Happy Contributing! 🚀**
