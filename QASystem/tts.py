import pyttsx3
import threading


class TextToSpeech:
    def __init__(self, voice: str = "default", rate: int = 170, volume: float = 1.0):
        self.engine = pyttsx3.init()
        self.set_voice(voice)
        self.set_rate(rate)
        self.set_volume(volume)

    def set_voice(self, voice: str):
        voices = self.engine.getProperty("voices")
        if voice == "female":
            self.engine.setProperty("voice", voices[1].id)
        elif voice == "male":
            self.engine.setProperty("voice", voices[0].id)
        else:
            # Default system voice
            self.engine.setProperty("voice", voices[0].id)

    def set_rate(self, rate: int):
        self.engine.setProperty("rate", rate)

    def set_volume(self, volume: float):
        self.engine.setProperty("volume", volume)  # 0.0 to 1.0

    def speak(self, text: str, async_mode: bool = True):
        if async_mode:
            threading.Thread(target=self._speak, args=(text,)).start()
        else:
            self._speak(text)

    def _speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
