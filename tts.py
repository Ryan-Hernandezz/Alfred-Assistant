import pyttsx3
import speech_recognition

#TTS voice rec
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

#function that converts TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()
    