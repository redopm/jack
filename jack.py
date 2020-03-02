#/usr/bin/python3
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess


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


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(['/usr/bin/gedit', file_name])



wishme()
while True:
    print("Listening...")
    text = get_audio()
    WAKE_UP = "hello jack"
    if text.count(WAKE_UP)> 0:
        speak("Hello Sir, what can i do for you ?")
        text = get_audio()

        NOTE_TERM = ["make a note", "write this down", "point out", "remember this", "hilight this", "write a note"]
        for phrese in NOTE_TERM:
            if phrese in text:
                speak("what would you like to "+str(phrese)+"?")
                note_text = get_audio()
                note(note_text)
                speak("I have done.")

        BYE = ['bye', 'stop', 'stop listening', "don't listen"]
        for phrese in BYE:
            if phrese in text:
                speak("Ok, have a nice day.")
                exit()
            else:
                speak("i'm sorry. ")
                
       






