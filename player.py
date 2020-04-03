import os
import pyttsx3
import speech_recognition as sr
import playsound

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

def play (text):
    return os.system("rhythmbox-client --play")
def pause (text):
    return os.system("rhythmbox-client --pause")
def next (text):
    return os.system("rhythmbox-client --next")
def prev(text):
    return os.system("rhythmbox-client --previous")
def printplay (text):
    return os.system("rhythmbox-client --print-playing")
def volup (text):
    return os.system("rhythmbox-client --volume-up")
def voldown (text):
    return os.system("rhythmbox-client --volume-down")
def repeat(text):
    return os.system("rhythmbox-client --repeat")
def norepeat (text):
    return os.system("rhythmbox-client --no-repeat")
def shuffle (text):
    return os.system("rhythmbox-client --shuffle")
def noshuf (text):
    return os.system("rhythmbox-client --no-shuffle")
def check (text):
    return os.system("rhythmbox-client --check-running")
speak("player is started !")
try:
    while True:
        text = get_audio()

        PLAY = ["play music", "open player", "play song", "start music player"]    
        for phrese in PLAY:
            if phrese in text:
                s= printplay(text)
                speak(str(s))
                play(text)

        PAUSE = ["pause music", "close player", "pause song", "stop music player", "stop music"]          
        for phrese in PAUSE:
            if phrese in text:
                pause(text)

        NEXT = ["next song", "next"]
        for phrese in NEXT:
            if phrese in text:           
                next(text)

        PREV = ["previous song", "previous", "come back"]
        for phrese in PREV:
            if phrese in text:           
                prev(text)

        REPEAT = ["repeat song", "repeat on"]
        for phrese in REPEAT:
            if phrese in text:           
                repeat(text)

        NOREP = ["no repeat song", "repeat off", "stop repeat"]
        for phrese in NOREP:
            if phrese in text:           
                norepeat(text)

        SHUFFLE = ["shuffle song", "shuffle on", "mixed"]
        for phrese in SHUFFLE:
            if phrese in text:           
                shuffle(text)

        NOSHUF = ["no shuffle song", "shuffle off", "do not mixed"]
        for phrese in NOSHUF:
            if phrese in text:                     
                noshuf(text)

        BYE = ['bye', 'stop listening', "don't listen"]
        for phrese in BYE:
            if phrese in text:
                speak("Ok, have a nice day.")
                pause(text)
                exit()
except Exception as e :
    print(e)


