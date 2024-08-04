# src/virtual_mouse.py

import cv2
import mediapipe as mp
import pyautogui
import math
from config.config import CLICK_THRESHOLD


class VirtualMouse:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def calculate_distance(self, point1, point2):
        """Calculate the Euclidean distance between two points."""
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    def calculate_hand_center(self, landmarks):
        """Calculate the center of the hand based on specific landmarks."""
        center_x = (landmarks[mp.solutions.hands.HandLandmark.WRIST].x +
                    landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP].x +
                    landmarks[mp.solutions.hands.HandLandmark.PINKY_MCP].x) / 3
        center_y = (landmarks[mp.solutions.hands.HandLandmark.WRIST].y +
                    landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP].y +
                    landmarks[mp.solutions.hands.HandLandmark.PINKY_MCP].y) / 3
        return center_x, center_y

    def is_fist(self, landmarks):
        """Determine if the hand is making a fist."""
        # Check if fingertips are close to their respective MCPs
        tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP,
        ]
        mcps = [
            self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
            self.mp_hands.HandLandmark.RING_FINGER_MCP,
            self.mp_hands.HandLandmark.PINKY_MCP,
        ]
        for tip, mcp in zip(tips, mcps):
            distance = self.calculate_distance(landmarks[tip], landmarks[mcp])
            if distance > CLICK_THRESHOLD:  # Use the threshold from settings
                return False
        return True

    def run(self):
        """Main loop for running the virtual mouse."""
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                continue

            # Flip the image horizontally for a later selfie-view display
            image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Process the image and find hands
            results = self.hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Calculate the center of the hand
                    center_x, center_y = self.calculate_hand_center(hand_landmarks.landmark)

                    # Map the center of the hand to screen coordinates
                    screen_width, screen_height = pyautogui.size()
                    x, y = int(center_x * screen_width), int(center_y * screen_height)

                    # Move the mouse
                    pyautogui.moveTo(x, y)

                    # Click if a fist is detected
                    if self.is_fist(hand_landmarks.landmark):
                        pyautogui.click()

                    # Draw landmarks on the hand
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # Display the image
            cv2.imshow('Virtual Mouse', image)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
