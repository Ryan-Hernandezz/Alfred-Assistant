from email import message
from email.base64mime import body_decode
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
import pyaudio
from twilio.rest import Client

#TTS voice rec
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

#function that converts TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function that greets user based on the time of day
def greeting():
    hr = datetime.datetime.now().hour
    if(hr >= 0 and hr < 12):
        speak("Good Morning Mister Hernandez")
        print("Good Morning Mister Hernandez")
    if(hr >= 12 and hr < 18):
        speak("Good Afternoon Mister Hernandez")
        print("Good Afternoon Mister Hernandez")
    else:
        speak("Good Evening Mister Hernandez")
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
            speak("Sorry Ryan, can you say that again")
            return "None"
        return phrase

speak("Alfred Loading...")
time.sleep(2)
greeting()

#main that calls other functions and listens for keywords
if __name__ == '__main__':
    while True:
        speak("What can I do for you? ")
        phrase = command().lower()

        if phrase == 0:
            continue

        if "goodbye Alfred" in phrase or "ok Alfred" in phrase or "thanks Alfred" in phrase or "thanks" in phrase:
            speak("With Pleasure.")
            exit()

        if "wikipedia" in phrase:
            speak("Retrieving results...")
            phrase = phrase.replace("wikipedia", "")
            results = wikipedia.summary(phrase, sentences = 4)
            speak("Here is what I found. ")
            speak(results)
        
        elif "open youtube" in phrase:
            webbrowser.open_new_tab("www.youtube.com")
            speak("Youtube now open")
            time.sleep(5)
        
        elif "open google" in phrase:
            webbrowser.open_new_tab("www.google.com")
            speak("Google now open")
            time.sleep(5)
        
        elif "open twitch" in phrase:
            webbrowser.open_new_tab("www.twitch.com")
            speak("Twitch now open")
            time.sleep(5)
        
        elif "time" in phrase:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {t}")
        
        elif "who are you?" in phrase:
            speak("Alfred. I'm here to assist you in anything and everything.")
        
        elif "who created you?" in phrase:
            speak("I was programmed by Ryan. ")
        
        elif "news" in phrase:
            webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            speak("Current world news")
            time.sleep(5)
        
        elif "open chess" in phrase:
            webbrowser.open_new_tab("https://www.chess.com/home")
            speak("Chess game open")
            time.sleep(5)

        elif "search" in phrase:
            phrase = phrase.replace("search", "")
            webbrowser.open(phrase)
            time.sleep(5)

        elif "shut down" in phrase:
            speak("Shutting down... Goodbye")
            subprocess.call(["shutdown", "/1"])
        
        elif "take note" in phrase:
            speak("Go ahead.")
            n = command()
            file = open("notes.txt", "w")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(f"({strTime}) ")
            file.write(n)

        elif "read notes" in phrase:
            speak("getting notes.")
            file = open("notes.txt", "r")
            speak(file.readlines(5))

        elif "weather" in phrase:
            apiKey = "6534ecd31781f4795e27d71f48c39f50"
            site_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            city = "Dallas"
            complete_url = site_url + "appid =" + apiKey + "&q =" + city
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))


        elif "send message" in phrase:
            contacts = [
                "mom": "+19722072911",
                "brittney": "+14699672783",
                "sergio": "+12146955418",
                "erick": "+12147381472",
                "ryan": "+19722072911"
            ],
            
            account_sid = "AC6079ef30fd375aa666d4694c302e7e0d"
            auth_token = "3e848df9fd9558d534574a9354a52007"
            speak("To who?")
            to = command()
            client = Client(account_sid, auth_token)
            message = client.messages.create(body = command(), from_ = "+19384855848", to = to)


            

time.sleep(3)
exit()
