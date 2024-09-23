import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

# Initialize the modules
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Eye-tracking setup
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for user voice commands and return the recognized text."""
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            listener.pause_threshold = 1
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Can you repeat?")
    except sr.RequestError:
        talk("Sorry, I'm having trouble connecting to the recognition service.")
    except Exception as e:
        talk("An error occurred.")
        print(f"Error: {e}")

    return command

def run_voice_commands(command):
    """Execute tasks based on voice commands."""
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time_str = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time_str)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

def run_eye_control():
    """Control the mouse using face landmarks detected from the camera."""
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

            if id == 1:  # Use the 1st point for controlling the cursor
                screen_x = int(screen_w * landmark.x)
                screen_y = int(screen_h * landmark.y)
                pyautogui.moveTo(screen_x, screen_y)

        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

        if (left_eye[0].y - left_eye[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(0.3)  # Short delay to prevent multiple clicks

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False  # Return False to exit the loop
    return True

# Main program loop
while True:
    command = take_command()

    if command:
        print(f"Command received: {command}")
        run_voice_commands(command)

        # Switch to eye control if command says 'mouse control'
        if 'mouse control' in command:
            talk('Switching to mouse control')
            while run_eye_control():  # Stay in eye control until 'q' is pressed
                pass

    # Allow the program to take a break and not overuse CPU resources
    time.sleep(1)

# Cleanup resources after exiting
cam.release()
cv2.destroyAllWindows()
