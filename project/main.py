import speech_recognition as sr
from voicecommand import send_to_flask
from voicecommand import get_voice_command, send_to_flask

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    send_to_flask(command)
except sr.UnknownValueError:
    print("Could not understand audio.")

if __name__ == "__main__":
    command = get_voice_command()
    if command:
        send_to_flask(command)
