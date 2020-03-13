#/usr/bin/python3
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import re
from pyowm import OWM
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
            print('You: ' +said+"\n")
        except Exception as e:
            speak("Please Say somthing... "+ str(e))
    return said.lower()

# wish good morning, good afternoon etc
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning !")
    elif hour>=12 and hour<18:
        speak("good afternoon !")
    else:
        speak("good evening !")

#write note 
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(['/usr/bin/gedit', file_name])

# play music with system player
'''def play(text):
    path = '/home/omprakash/Music/song/english\ songs/'
    folder = path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
            speak('What song shall I play Sir?')
            mysong = get_audio()'''

wishme()
#common_question.chat()
while True:
    print("Listening...")
    text = get_audio()
    WAKE_UP = "hello"
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

        APP = ["open", " "]
        for phrese in APP:
            if phrese in text:
                os.system(text)
                speak("your application " +text+ " is opening.")

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
            y = w.get_sunrise_time('iso')
            z = w.get_sunset_time('iso')  
            speak('weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius and sunrise time is %s and sunset time is %s' % (city, k, x['temp_max'], x['temp_min'], y, z))
    

        BYE = ['bye', 'stop', 'stop listening', "don't listen"]
        for phrese in BYE:
            if phrese in text:
                speak("Ok, have a nice day.")
                exit()