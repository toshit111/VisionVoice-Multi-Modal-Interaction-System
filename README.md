# VisionVoice: Multi-Modal Interaction System

VisionVoice is an innovative multi-modal interaction system that combines voice recognition and eye tracking to control mouse movements and execute commands. This project enhances user interaction by allowing hands-free control through voice and eye movements.

## Features

- **Voice Command Recognition**: Understands commands using the `speech_recognition` library.
- **Text-to-Speech**: Provides vocal feedback using `pyttsx3`.
- **YouTube Playback**: Plays songs directly from YouTube based on voice commands.
- **Information Retrieval**: Fetches current time and information from Wikipedia.
- **Eye Tracking for Mouse Control**: Uses `mediapipe` for real-time eye tracking to control the cursor and perform clicks.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- SpeechRecognition
- pyttsx3
- PyWhatKit
- Wikipedia API
- PyJokes


## Usage
1. Clone the repository:

git clone [YOUR_GITHUB_LINK]
cd VisionVoice

2. Run the main script:

python vision_voice.py

3. Follow the voice prompts to interact with the system. You can:

Ask for the current time.
Request a song to play on YouTube.
Retrieve information about a person or topic.
Control the mouse using eye movements (activate by saying "mouse control").

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe pyautogui SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
