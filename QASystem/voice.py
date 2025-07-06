import speech_recognition as sr
import pyttsx3

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()

    def listen(self) -> str:
        with self.microphone as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            print("Listening...")
            audio = self.recognizer.listen(mic)
        try:
            text = self.recognizer.recognize_google(audio)
            return text.strip().lower()
        except Exception:
            return ""

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
