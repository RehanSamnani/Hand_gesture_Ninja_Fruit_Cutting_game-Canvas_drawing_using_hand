import cv2
import time
import random
import mediapipe as mp
import math
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Global variables
curr_Frame = 0
prev_Frame = 0
delta_time = 0

# Game Mode Variables
next_Time_to_Spawn = 0
Speed = [0, 5]
Fruit_Size = 30
Spawn_Rate = 1
Score = 0
Lives = 15
Difficulty_level = 1
game_Over = False

slash = np.array([[]], np.int32)
slash_Color = (255, 255, 255)
slash_length = 19

w = h = 0

Fruits = []

# Drawing Mode Variables
drawing_mode_active = False
drawing_color = (0, 255, 0)  # Default green
drawing_shape = "free"  # "line", "circle", or "free"
canvas = None
prev_point = None
in_drawing = False
draw_start_point = None
brush_size = 3

# Color options: (B, G, R)
COLORS = {
    "Red": (0, 0, 255),
    "Green": (0, 255, 0),
    "Blue": (255, 0, 0),
    "Yellow": (0, 255, 255),
    "Cyan": (255, 255, 0),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0)
}


def draw_main_menu(frame, w, h):
    """Draw the main menu with two options - clean and responsive"""
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, h), (15, 15, 20), -1)
    frame = cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)
    
    # Add gradient effect with semi-transparent bars
    cv2.rectangle(frame, (0, 0), (w, 150), (30, 30, 40), -1)
    cv2.rectangle(frame, (0, h-100), (w, h), (30, 30, 40), -1)
    
    # Title - Centered
    title = "HAND GESTURE APP"
    title_size = cv2.getTextSize(title, cv2.FONT_HERSHEY_TRIPLEX, 1.8, 3)[0]
    title_x = (w - title_size[0]) // 2
    cv2.putText(frame, title, (title_x, 80), cv2.FONT_HERSHEY_TRIPLEX, 1.8, (0, 255, 255), 3)
    
    # Subtitle
    subtitle = "Choose Your Mode"
    subtitle_size = cv2.getTextSize(subtitle, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    subtitle_x = (w - subtitle_size[0]) // 2
    cv2.putText(frame, subtitle, (subtitle_x, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
    
    # Button dimensions
    btn_width = min(600, w - 100)
    btn_height = 140
    btn_x_start = (w - btn_width) // 2
    
    # Option 1: Game Button
    game_btn_y = 200
    cv2.rectangle(frame, (btn_x_start, game_btn_y), (btn_x_start + btn_width, game_btn_y + btn_height), (25, 120, 200), -1)
    cv2.rectangle(frame, (btn_x_start, game_btn_y), (btn_x_start + btn_width, game_btn_y + btn_height), (100, 200, 255), 4)
    
    game_title = "1. NINJA FRUIT GAME"
    game_title_size = cv2.getTextSize(game_title, cv2.FONT_HERSHEY_DUPLEX, 1.2, 2)[0]
    game_title_x = btn_x_start + (btn_width - game_title_size[0]) // 2
    cv2.putText(frame, game_title, (game_title_x, game_btn_y + 50), cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)
    
    game_desc = "Cut fruits with your hand gestures"
    game_desc_size = cv2.getTextSize(game_desc, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0]
    game_desc_x = btn_x_start + (btn_width - game_desc_size[0]) // 2
    cv2.putText(frame, game_desc, (game_desc_x, game_btn_y + 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 220, 220), 1)
    
    # Option 2: Drawing Button
    draw_btn_y = 380
    cv2.rectangle(frame, (btn_x_start, draw_btn_y), (btn_x_start + btn_width, draw_btn_y + btn_height), (150, 50, 180), -1)
    cv2.rectangle(frame, (btn_x_start, draw_btn_y), (btn_x_start + btn_width, draw_btn_y + btn_height), (200, 100, 255), 4)
    
    draw_title = "2. DRAWING MODE"
    draw_title_size = cv2.getTextSize(draw_title, cv2.FONT_HERSHEY_DUPLEX, 1.2, 2)[0]
    draw_title_x = btn_x_start + (btn_width - draw_title_size[0]) // 2
    cv2.putText(frame, draw_title, (draw_title_x, draw_btn_y + 50), cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)
    
    draw_desc = "Draw shapes and create art freely"
    draw_desc_size = cv2.getTextSize(draw_desc, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0]
    draw_desc_x = btn_x_start + (btn_width - draw_desc_size[0]) // 2
    cv2.putText(frame, draw_desc, (draw_desc_x, draw_btn_y + 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 220, 220), 1)
    
    # Instructions at bottom - Multiple lines for clarity
    inst_y = h - 70
    inst1 = "Press 1 = Game Mode  |  Press 2 = Drawing Mode  |  Press Q = Quit"
    inst1_size = cv2.getTextSize(inst1, cv2.FONT_HERSHEY_SIMPLEX, 0.65, 1)[0]
    inst1_x = (w - inst1_size[0]) // 2
    cv2.putText(frame, inst1, (inst1_x, inst_y), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 100), 1)
    
    inst2 = "Use your webcam hand gestures to control the application"
    inst2_size = cv2.getTextSize(inst2, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)[0]
    inst2_x = (w - inst2_size[0]) // 2
    cv2.putText(frame, inst2, (inst2_x, inst_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 200, 255), 1)
    
    return frame


def draw_drawing_ui(frame, w, h, drawing_shape, drawing_color):
    """Draw the compact UI for drawing mode - minimal top bar, large canvas"""
    
    # Compact Top Control Panel - Reduced height
    panel_height = 60
    cv2.rectangle(frame, (0, 0), (w, panel_height), (20, 20, 30), -1)
    cv2.rectangle(frame, (0, 0), (w, panel_height), (100, 150, 200), 2)
    
    # Title on left
    cv2.putText(frame, "DRAW MODE", (15, 35), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 1)
    
    # Shape indicators - compact
    shape_status = f"Shape: {drawing_shape.upper()}"
    cv2.putText(frame, shape_status, (250, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 100), 1)
    
    # Color indicator - compact
    color_name = [k for k, v in COLORS.items() if v == drawing_color][0] if drawing_color in COLORS.values() else "Custom"
    cv2.putText(frame, f"Color: {color_name}", (500, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, drawing_color, 1)
    
    # Quick keys on right
    cv2.putText(frame, "L=Line O=Circle F=Free | R/G/B/Y=Color | C=Clear M=Menu Q=Quit", 
                (650, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 255), 1)
    
    return frame


def get_hand_position(hand_landmarks, img_w, img_h):
    """Get the position of the index finger tip"""
    index_tip = hand_landmarks.landmark[8]
    return (int(index_tip.x * img_w), int(index_tip.y * img_h))


def get_thumb_position(hand_landmarks, img_w, img_h):
    """Get the position of the thumb tip"""
    thumb_tip = hand_landmarks.landmark[4]
    return (int(thumb_tip.x * img_w), int(thumb_tip.y * img_h))


def is_pinching(hand_landmarks):
    """Check if thumb and index finger are pinching"""
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    distance = math.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
    return distance < 0.05


# ========== GAME FUNCTIONS ==========

def Spawn_Fruits():
    global Fruits
    fruit = {}
    random_x = random.randint(15, 600)
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fruit["Color"] = random_color
    fruit["Curr_position"] = [random_x, 440]
    fruit["Next_position"] = [0, 0]
    Fruits.append(fruit)


def Fruit_Movement(Fruits, speed, img, w, h):
    global Lives

    for fruit in Fruits[:]:
        if (fruit["Curr_position"][1]) < 20 or (fruit["Curr_position"][0]) > 650:
            Lives = Lives - 1
            Fruits.remove(fruit)
            continue

        cv2.circle(img, tuple(fruit["Curr_position"]), Fruit_Size, fruit["Color"], -1)
        fruit["Next_position"][0] = fruit["Curr_position"][0] + speed[0]
        fruit["Next_position"][1] = fruit["Curr_position"][1] - speed[1]
        fruit["Curr_position"] = fruit["Next_position"]


def distance(a, b):
    d = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    return int(d)


def reset_game():
    """Reset all game variables"""
    global Score, Lives, Difficulty_level, game_Over, Fruits, Speed, Spawn_Rate, slash, next_Time_to_Spawn
    global slash_Color
    Score = 0
    Lives = 15
    Difficulty_level = 1
    game_Over = False
    Fruits.clear()
    Speed = [0, 5]
    Spawn_Rate = 1
    slash = np.array([[]], np.int32)
    slash_Color = (255, 255, 255)
    next_Time_to_Spawn = time.time()


# ========== GAME MODE ==========

def play_game_mode(cap):
    """Main game loop for Ninja Fruit Game"""
    global Score, Lives, Difficulty_level, game_Over, Fruits, Speed, Spawn_Rate, slash, slash_Color
    global curr_Frame, prev_Frame, next_Time_to_Spawn, w, h
    
    reset_game()
    window_name = "Hand Gesture App"
    
    while True:
        success, img = cap.read()
        if not success:
            continue
        
        h, w, c = img.shape
        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                for id, lm in enumerate(hand_landmarks.landmark):
                    if id == 8:
                        index_pos = (int(lm.x * w), int(lm.y * h))
                        cv2.circle(img, index_pos, 18, slash_Color, -1)
                        slash = np.append(slash, index_pos)

                        while len(slash) >= slash_length:
                            slash = np.delete(slash, len(slash) - slash_length, 0)

                        for fruit in Fruits[:]:
                            d = distance(index_pos, fruit["Curr_position"])
                            if (d < Fruit_Size):
                                Score = Score + 100
                                slash_Color = fruit["Color"]
                                Fruits.remove(fruit)

        if Score % 1000 == 0 and Score != 0:
            Difficulty_level = (Score / 1000) + 1
            Difficulty_level = int(Difficulty_level)
            Spawn_Rate = Difficulty_level * 4 / 5
            Speed[0] = Speed[0] * Difficulty_level
            Speed[1] = int(5 * Difficulty_level / 2)

        if Lives <= 0:
            game_Over = True

        slash_reshaped = slash.reshape((-1, 1, 2)) if len(slash) > 0 else np.array([[[0, 0]]], np.int32)
        cv2.polylines(img, [slash_reshaped], False, slash_Color, 15, 0)

        curr_Frame = time.time()
        delta_Time = curr_Frame - prev_Frame
        FPS = int(1 / delta_Time) if delta_Time > 0 else 0
        prev_Frame = curr_Frame
        
        # Draw HUD Panel at top
        cv2.rectangle(img, (0, 0), (w, 90), (20, 20, 30), -1)
        cv2.rectangle(img, (0, 0), (w, 90), (100, 150, 200), 2)
        
        # Title
        cv2.putText(img, "NINJA FRUIT GAME", (w//2 - 140, 35), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        
        # Stats
        cv2.putText(img, f"Score: {Score}", (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 200, 255), 2)
        cv2.putText(img, f"Lives: {Lives}", (350, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 150, 255), 2)
        cv2.putText(img, f"Level: {Difficulty_level}", (700, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 200, 255), 2)
        cv2.putText(img, f"FPS: {FPS}", (w-150, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Bottom controls panel
        cv2.rectangle(img, (0, h-70), (w, h), (20, 20, 30), -1)
        cv2.rectangle(img, (0, h-70), (w, h), (100, 150, 200), 2)
        
        inst_line1 = "HOW TO PLAY: Move your hand to position cursor | Touch (cut) falling fruits to score points"
        inst_line2 = "Controls: M = Return to Menu | Q = Quit | Avoid missing fruits or you lose lives!"
        
        inst_size1 = cv2.getTextSize(inst_line1, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)[0]
        inst_x1 = (w - inst_size1[0]) // 2
        cv2.putText(img, inst_line1, (inst_x1, h-40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 200, 255), 1)
        
        inst_size2 = cv2.getTextSize(inst_line2, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)[0]
        inst_x2 = (w - inst_size2[0]) // 2
        cv2.putText(img, inst_line2, (inst_x2, h-12), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 200, 255), 1)

        if not game_Over:
            if time.time() > next_Time_to_Spawn:
                Spawn_Fruits()
                next_Time_to_Spawn = time.time() + (1 / Spawn_Rate)
            Fruit_Movement(Fruits, Speed, img, w, h)
        else:
            cv2.putText(img, "GAME OVER!", (int(w * 0.25), int(h * 0.4)), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 3)
            cv2.putText(img, f"Final Score: {Score}", (int(w * 0.2), int(h * 0.55)), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 255), 2)

        cv2.imshow(window_name, img)
        key = cv2.waitKey(5) & 0xFF
        if key == ord('m'):
            return "menu"
        elif key == ord('q'):
            return "quit"


# ========== DRAWING MODE ==========

def play_drawing_mode(cap):
    """Drawing mode with hand gesture support - enhanced with shape modes"""
    global drawing_color, drawing_shape, prev_point, in_drawing, canvas, w, h, draw_start_point, brush_size
    
    canvas = np.zeros((h, w, 3), dtype=np.uint8)
    prev_point = None
    draw_start_point = None
    window_name = "Hand Gesture App"
    
    while True:
        success, img = cap.read()
        if not success:
            continue
        
        h, w, c = img.shape
        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # Draw canvas on frame with emphasis (30% camera, 70% canvas for visibility)
        if canvas is not None:
            img = cv2.addWeighted(img, 0.3, canvas, 0.7, 0)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_pos = get_hand_position(hand_landmarks, w, h)
                pinching = is_pinching(hand_landmarks)
                
                # Draw hand skeleton
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                # Draw index finger indicator
                indicator_color = (0, 255, 0) if not pinching else (0, 0, 255)
                cv2.circle(img, index_pos, 12, indicator_color, -1)
                cv2.circle(img, index_pos, 12, (255, 255, 255), 2)
                
                if pinching:
                    if draw_start_point is None:
                        # Start drawing
                        draw_start_point = index_pos
                        prev_point = index_pos
                        in_drawing = True
                    
                    if drawing_shape == "free":
                        # Freehand drawing - continuous line
                        if prev_point is not None and prev_point != index_pos:
                            cv2.line(canvas, prev_point, index_pos, drawing_color, 5)
                            cv2.line(img, prev_point, index_pos, drawing_color, 5)
                        prev_point = index_pos  # Update AFTER drawing, not before
                    
                    elif drawing_shape == "line":
                        # Always update prev_point to current position for line mode
                        prev_point = index_pos
                        # Draw line from start to current position (update in real-time)
                        temp_img = img.copy()
                        cv2.line(temp_img, draw_start_point, index_pos, drawing_color, 5)
                        
                        # Show preview
                        cv2.circle(temp_img, draw_start_point, 10, (100, 255, 100), -1)
                        cv2.circle(temp_img, index_pos, 8, (0, 255, 0), 2)
                        img = temp_img
                    
                    elif drawing_shape == "circle":
                        # Always update prev_point to current position for circle mode
                        prev_point = index_pos
                        # Draw circle from start point with radius based on drag distance
                        radius = int(math.sqrt((index_pos[0] - draw_start_point[0])**2 + 
                                             (index_pos[1] - draw_start_point[1])**2))
                        temp_img = img.copy()
                        cv2.circle(temp_img, draw_start_point, radius, drawing_color, 5)
                        cv2.circle(temp_img, draw_start_point, 10, (100, 255, 100), -1)
                        cv2.circle(temp_img, index_pos, 8, (0, 255, 0), 2)
                        img = temp_img
                
                else:
                    # Release - finalize drawing and save to canvas
                    if in_drawing and draw_start_point is not None:
                        if drawing_shape == "line":
                            cv2.line(canvas, draw_start_point, prev_point, drawing_color, 5)
                        elif drawing_shape == "circle":
                            radius = int(math.sqrt((prev_point[0] - draw_start_point[0])**2 + 
                                                 (prev_point[1] - draw_start_point[1])**2))
                            cv2.circle(canvas, draw_start_point, radius, drawing_color, 5)
                    
                    draw_start_point = None
                    prev_point = None
                    in_drawing = False
        
        # Draw UI (minimal, at top and bottom)
        img = draw_drawing_ui(img, w, h, drawing_shape, drawing_color)
        
        cv2.imshow(window_name, img)
        key = cv2.waitKey(5) & 0xFF
        
        if key == ord('c'):  # Clear canvas
            canvas = np.zeros((h, w, 3), dtype=np.uint8)
            prev_point = None
            draw_start_point = None
        elif key == ord('m'):  # Return to menu
            return "menu"
        elif key == ord('q'):  # Quit
            return "quit"
        elif key == ord('l'):  # Switch to line
            drawing_shape = "line"
        elif key == ord('o'):  # Switch to circle
            drawing_shape = "circle"
        elif key == ord('f'):  # Switch to free drawing
            drawing_shape = "free"
        elif key == ord('r'):  # Red
            drawing_color = COLORS["Red"]
        elif key == ord('g'):  # Green
            drawing_color = COLORS["Green"]
        elif key == ord('b'):  # Blue
            drawing_color = COLORS["Blue"]
        elif key == ord('y'):  # Yellow
            drawing_color = COLORS["Yellow"]


# ========== MAIN MENU LOOP ==========

cap = cv2.VideoCapture(0)

# Create window and set to fullscreen
window_name = "Hand Gesture App"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

menu_active = True
while menu_active:
    success, img = cap.read()
    if not success:
        continue
    
    h, w, c = img.shape
    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Draw menu
    img = draw_main_menu(img, w, h)
    
    cv2.imshow(window_name, img)
    key = cv2.waitKey(5) & 0xFF
    
    if key == ord('1'):
        result = play_game_mode(cap)
        if result == "quit":
            menu_active = False
    elif key == ord('2'):
        result = play_drawing_mode(cap)
        if result == "quit":
            menu_active = False
    elif key == ord('q'):
        menu_active = False

cap.release()
cv2.destroyAllWindows()
