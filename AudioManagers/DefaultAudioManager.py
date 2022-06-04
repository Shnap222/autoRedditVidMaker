from . import audio_config
import pyttsx3


class DefaultAudioManager:

    def __init__(self):
        self.convertor = pyttsx3.init()
        self.convertor.setProperty('rate', audio_config.RATE)

    def record_text_to_file(self, text: str, path: str):
        self.convertor.save_to_file(text, f'{path}.mp3')

        self.convertor.runAndWait()
