import numpy as np
import speech_recognition as sr
import os
from gtts import gTTS

# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("listening...")
             audio = recognizer.listen(mic)
        try:
             self.text = recognizer.recognize_google(audio)
             print("me --> ", self.text)
        except:
             print("me -->  ERROR")

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("aud.mp3")
        os.system("start aud.mp3")
        os.remove("aud.mp3")

# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="Anna")
    while True:
        ai.speech_to_text()

        if ai.wake_up(ai.text) is True:
             aud = "Hello I am Anna, what can I do for you?"
             ai.text_to_speech(aud)
