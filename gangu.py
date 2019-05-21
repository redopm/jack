import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#print(voices[0],id)
#engine.setProperty('voice',voices[0].id)
engine = pyttsx3.init()
#engine.say('Good morning.')


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def Wishme():
	hour = int(datatime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning sir!")

	elif hour>=12 and hour<18:
		speak("Good Afternoon sir!")

	else:
		speak("Good Evening sir!")

	speak("I am Gangu , your personal assistant, how may i help you!")

def takecommand():
	#
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, Lanuage='en-in')
		print("User said:", query)

	except Exception as e:
		#print(e)
		print("Say that again Please...")
		return "None"
	return query

if __name__=="__main__":
	Wishme()
	while true:
		query = takecommand().lower()
		# logic 

		if "wikipedia" in query:
			speak('Searching on wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 2)
			speak("According to wikipedia")
			print(results)
			speak(results)

		elif "open google" in query:
			webbrowser.open("google.com")

		elif "open youtube" in query:
			webbrowser.open("youtube.com")

		elif "play music" in query:
			music_dir = '/home//omprakash//music'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak("sir, the time is", strTime)

		elif "open notepad" in query:
			notepadPath = "/usr/bin/gedit"
			os.startfile(notepadPath)
			

