#/usr/bin/python3
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            speak("Please Say somthing... "+ str(e))
    return said.lower()

    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning !")
    elif hour>=12 and hour<18:
        speak("good afternoon !")
    else:
        speak("good evening !")


wishme()
WAKE_UP = "ok jack"
while True:
    print("Listening...")
    text = get_audio()
    if text.count(WAKE_UP)> 0:
        speak("what can i do for you ?")
        text = get_audio()
    






