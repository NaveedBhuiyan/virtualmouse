# Virtual Mouse with Hand Gesture Control

This project implements a virtual mouse using computer vision and hand gesture recognition. The application utilizes the [MediaPipe](https://mediapipe.dev/) library to detect hand landmarks and the [PyAutoGUI](https://pyautogui.readthedocs.io/) library to control the mouse based on the detected gestures. The primary gesture for interaction is making a fist to trigger a mouse click.

## Features

- **Hand Tracking**: Real-time hand tracking using your webcam.
- **Gesture Recognition**: Detects hand gestures to perform actions such as mouse clicks.
- **Cursor Control**: Moves the cursor based on the center position of your hand.
- **Fist Gesture Click**: Performs a mouse click when a fist gesture is detected.

## Screenshots

### Hand Tracking

![Hand Tracking](images/hand_tracking.png)

## Directory Structure

```
project_root/
│
├── src/
│ └── virtual_mouse.py # VirtualMouse class definition
├── main.py # Entry point for the application
└── config/config.py # Configuration settings 
```


## Prerequisites

- Python 3.x
- A webcam

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
```

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt
```
```
python main.py
```

# Usage
The application will open your webcam and start tracking your hand.
Move your hand to control the mouse cursor.
Make a fist gesture to perform a mouse click.
Press q to quit the application.

# Configuration
Click Threshold: Adjust the click threshold in config/settings.py to fine-tune the sensitivity of the fist gesture detection. This might need to be calibrated depending on your specific webcam setup.

CLICK_THRESHOLD = 0.05  # Adjust this threshold based on your setup

# Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
MediaPipe

PyAutoGUI

Contact

For any questions, feel free to reach out to naveedbhuiyan21@gmail.com






