import os
import playsound
import speech_recognition as sr
import pyttsx3
import time

def PLAY(text):
    os.system("rhythmbox-client --play")
def PAUSE(text):
    os.system("rhythmbox-client --pause")
def NEXT(text):
    os.system("rhythmbox-client --next")
def PREV(text):
    os.system("rhythmbox-client --previous")
def QUIT(text):
    os.system("rhythmbox-client --quit")
def VOL_UP(text):
    os.system("rhythmbox-client --volume-up")
def VOL_DOWN(text):
    os.system("rhythmbox-client --volume-down")
def print_vol(text):
    os.system("rhythmbox-client --print-volume")
def REP(text):
    os.system("rhythmbox-client --repeat")
def NO_REP(text):
    os.system("rhythmbox-client --no-repeat")
def SHUF(text):
    os.system("rhythmbox-client --shuffle")
def NO_SHUF(text):
    os.system("rhythmbox-client --no-shuffle")                                                           

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
            if (os.system("rhythmbox-client --check-running")==True):
                speak("Please say somthing.."+str(e))
            
    return said.lower()

speak("you want to listen music then say play music")
while True:  
    text = get_audio()
    play_song = ["play music", "can you play a song", "play song", "play", "start"]
    for phrese in play_song:
        if phrese in text:
            PLAY(text)
            speak(str(os.system("rhythmbox-client --print-playing")))

    pause_song = ["pause music", " can you pause", "stop", "stop playing", "pause"]
    for phrese in pause_song:
        if phrese in text:
            PAUSE(text)  

    next_song = ["next please", " can you play next song", "next song", "next"]
    for phrese in next_song:
        if phrese in text:
            NEXT(text)

    prev_song = ["previous please", " can you play previous song", "previous song", "previous", "come back"]
    for phrese in prev_song:
        if phrese in text:
            PREV(text)

    BYE = ["bye", "quit", "band kr do"]
    for phrese in BYE:
        if phrese in text:
            exit()

    SHUF = ["shuffle on", "mixed on", "shuffled"]
    for phrese in BYE:
        if phrese in text:
            SHUF(text)

    No_Shuffle = ["shuffle off", "no mixed", "do not shuffled"]
    for phrese in BYE:
        if phrese in text:
            NO_SHUF(text)

    Repeat = ["repeat on", "one song only", "bar bar ek hi song chalao"]
    for phrese in BYE:
        if phrese in text:
            REP(text)

    No_Repeat = ["repeat off", "all songs play", "one by one"]
    for phrese in BYE:
        if phrese in text:
            NO_REP(text)

    VolUp = ["volume up", "increase sound", "sound up", "fast sound"]
    for phrese in BYE:
        if phrese in text:
            VOL_UP(text)

    VolDown = ["volume down", "decrease sound", "sound down", "slow sound"]
    for phrese in BYE:
        if phrese in text:
            VOL_DOWN(text)


