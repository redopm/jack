import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3
import datetime


# play music with system player
def play(text):
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
            mysong = get_audio()