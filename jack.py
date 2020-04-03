#/usr/bin/python3
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import re
import wikipedia
from pyowm import OWM
import webbrowser

#import common_question

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

# wish good morning, good afternoon etc
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning sir !")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening sir !")

#write note 
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(['/usr/bin/gedit', file_name])


# any question you can ask
def askme(text):
    reg_ex = re.search('about (.*)', text)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            ny = wikipedia.summary(topic, sentences = 3)
            #content = ny.content[:500].encode('utf-8')
            speak(ny)
    except Exception as e:
            print(e)
            speak(e)
wishme()
#common_question.chat()
while True:
    
        speak("what can I do for you ?")
        text = get_audio()

        ASKME = ["what about", "tell me about", "do you know about", "can i know about", "who is"]
        for phrese in ASKME:
            if phrese in text:
                askme(text)
        
        NOTE_TERM = ["make a note", "write this down", "point out", "remember this", "hilight this", "write a note"]
        for phrese in NOTE_TERM:
            if phrese in text:
                speak("what would you like to "+str(phrese)+"?")
                note_text = get_audio()
                note(note_text)
                speak("I have done.")

        APP = ["open", "launch"]
        for phrese in APP:
            reg_ex = re.search('open (.*)', text)
            if reg_ex:
                appname = reg_ex.group(1)
                os.system(appname)
                speak("your application " +appname+ " is opened.")
            elif appname == "google chrome":
                os.system("google-chrome")
                speak("your application google chrome is opened.")
            elif appname =="terminal":
                os.system("gnome-terminal")
                speak("your application terminal is opened.")
            else:
                speak("sorry! Please try again an other name.")
                break
                

        TIME = ["what is time", "time please", "current time", "tell me the current time"]
        for phrese in TIME:
            if phrese in text:
                now = datetime.datetime.now()
                speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

        Weather = ['current weather', 'What is weather', 'weather', "What is the weather"]
        for phrese in text:
            reg_ex = re.search('weather in (.*)', text)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_detailed_status()
                x = w.get_temperature(unit='celsius')
                y = w.get_rain() 
                z = w.get_sunset_time("utc")  
                speak('weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius and sunrise time is %s and sunset time is %s' % (city, k, x['temp_max'], x['temp_min'], y, z))
                break

        BYE = ['bye', 'stop', 'stop listening', "don't listen"]
        for phrese in BYE:
            if phrese in text:
                speak("Ok, have a nice day.")
                exit()

        SEARCH = ["search on google", "google search", "can you search for me ", "can you search on google", "google"]
        for phrese in SEARCH:
            reg_ex = re.search('search on(.*)', text)
            if reg_ex:
                query = reg_ex.group(1)
                q="https://www.google.com/search?q="+ str(query)
                webbrowser.open(q)
                speak("your quary is"+str(query)+"open in your default browser")
                break

        PLAY = ["play music", "open player", "play song", "start music player"]
        import player
        for phrese in PLAY:
            if phrese in text:
                player.PLAY(text)







