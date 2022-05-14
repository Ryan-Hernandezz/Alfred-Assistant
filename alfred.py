from email.mime import audio
import speech_recognition as sp
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import wolframalpha
import requests
import tts

#function that greets user based on the time of day
def greeting():
    hr = datetime.datetime.now().hour
    if(hr >= 0 and hr < 12):
        tts.speak("Good Morning Mister Hernandez")
        print("Good Morning Mister Hernandez")
    if(hr >= 12 and hr < 18):
        tts.speak("Good Afternoon Mister Hernandez")
        print("Good Afternoon Mister Hernandez")
    else:
        tts.speak("Good Evening Mister Hernandez")
        print("Good Evening Mister Hernandez")

#function that listens and gets command from user
def command():
    rec = sp.Recognizer()
    with sp.Microphone() as source:
        print("I am listening...")
        audio = rec.listen(source)

        try:
            phrase = rec.recognize_google(audio, language='en-in')
            print(f"Ryan said: {phrase}\n")
        
        except Exception as e:
            tts.speak("Sorry Ryan, can you say that again")
            return "None"
        return phrase

tts.speak("Alfred Loading...")
time.sleep(2)
greeting()

#main that calls other functions and listens for keywords
if __name__ == '__main__':
    while True:
        tts.speak("What can I do for you? ")
        phrase = command().lower()

        if phrase == 0:
            continue

        if "goodbye Alfred" in phrase or "ok Alfred" in phrase or "thanks Alfred" in phrase or "thanks" in phrase:
            tts.speak("With Pleasure.")
            exit()

        if "wikipedia" in phrase:
            tts.speak("Retrieving results...")
            phrase = phrase.replace("wikipedia", "")
            results = wikipedia.summary(phrase, sentences = 4)
            tts.speak("Here is what I found. ")
            tts.speak(results)
        
        elif "open youtube" in phrase:
            webbrowser.open_new_tab("www.youtube.com")
            tts.speak("Youtube now open")
            time.sleep(5)
        
        elif "open google" in phrase:
            webbrowser.open_new_tab("www.google.com")
            tts.speak("Google now open")
            time.sleep(5)
        
        elif "open twitch" in phrase:
            webbrowser.open_new_tab("www.twitch.com")
            tts.speak("Twitch now open")
            time.sleep(5)
        
        elif "time" in phrase:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            tts.speak(f"Current time is {t}")
        
        elif "who are you?" in phrase:
            tts.speak("Alfred. I'm here to assist you in anything and everything.")
        
        elif "who created you?" in phrase:
            tts.speak("I was programmed by Ryan. ")
        
        elif "news" in phrase:
            webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            tts.speak("Current world news")
            time.sleep(5)
        
        elif "open chess game" in phrase:
            webbrowser.open_new_tab("https://www.chess.com/home")
            tts.speak("Chess game open")
            time.sleep(5)

        elif "search" in phrase:
            phrase = phrase.replace("search", "")
            webbrowser.open(phrase)
            time.sleep(5)

        elif "shut down" in phrase:
            tts.speak("Shutting down... Goodbye")
            subprocess.call(["shutdown", "/1"])


time.sleep(3)
exit()
