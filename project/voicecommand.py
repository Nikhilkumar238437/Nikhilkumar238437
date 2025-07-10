import speech_recognition as sr
import requests

def get_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Speak your command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("✅ You said:", command)
        return command
    except sr.UnknownValueError:
        print("❌ Could not understand your command.")
        return None
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")
        return None

def send_to_flask(command):
    url = "http://127.0.0.1:5000/voice"
    headers = {"Content-Type": "application/json"}
    payload = {"command": command}

    try:
        response = requests.post(url, json=payload, headers=headers)
        print("📡 Server replied:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ Could not connect to Flask server:", e)
