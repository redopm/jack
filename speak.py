#!/bin/python
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    filename = '/home/omprakash/ganggu/good.mp3'

    # Save audio data
    f = open(filename, 'wb+')
    f.write(sound_bytes)
    f.close()
    #tts.save("/home/omprakash/gangu/good.mp3")
    #os.system("/home/omprakash/gangu/good.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
    	print("Say something!")
    	#audio = r.listen(source)
    	audio=r.adjust_for_ambient_noise(source, duration=5)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(1)
speak("Hi Frank, what can I do for you?")
while True:
    data = recordAudio()
    jarvis(data)
