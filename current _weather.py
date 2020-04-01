import time 
import playsound
import speech_recognition as sr
from pyowm import OWM
import re
import pyttsx3
from pyowm.caches.lrucache import LRUCache
from datetime import datetime 
import pytz 
  
  
tz_INDIA = pytz.timezone('Asia/Kolkata')  
datetime_INDIA = datetime.now(tz_INDIA) 
date = datetime_INDIA.strftime("%H:%M:%S")

MONTHS = ['january', '']
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
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
            print(Exception, e)
    return said.lower()

def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    mount = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month - MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found - word.find(ext)
                if found>0:
                    try:
                        day - int(word[:found])
                    except:
                        pass
    if month < today.month and month != -1:
        year = year+1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week - today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif +=7


def weather():
    API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa'
    owm = OWM(API_key)
    #cache = LRUCache()
    obs = owm.weather_at_place('Jaipur')
    w = obs.get_weather(date)
    k = w.get_detailed_status()
    x = w.get_reference_time(timeformat='iso') 
    print(w)

weather()



'''    return 
text = get_audio()

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
        
'''