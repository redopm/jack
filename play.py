import os
import playsound
import speech_recognition as sr
import pyttsx3
import time


# text to speak by jack 
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait() 
    print("Jack: "+ text)

# text recognise by  jack
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print('You: ' +said)
        except Exception as e:
            print("Please Say somthing... "+ str(e))
    return said.lower()
while True:
    text = get_audio()

    PLAY = ["play music", " can you play a song", "play song", "play"," start"]
    for phrese in PLAY:
        if phrese in text:
            os.system("rhythmbox-client --play")

    PAUSE = ["pause music", " can you pause", "stop", "stop playing", "pause"]
    for phrese in PAUSE:
        if phrese in text:
            os.system("rhythmbox-client --pause")

    NEXT = ["next please", " can you play next song", "next song", "next"]
    for phrese in NEXT:
        if phrese in text:
            os.system("rhythmbox-client --next")

    PREV = ["previous please", " can you play previous song", "previous song", "previous"]
    for phrese in PREV:
        if phrese in text:
            os.system("rhythmbox-client --previous")
