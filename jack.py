#/usr/bin/python3
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3

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
            print("Please Say somthing... "+ str(e))
            speak("Please say somethng")
    return said

text = get_audio()
if "hello" in text:
    speak("hello, how are you ?")




