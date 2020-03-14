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
         if mysong:
                flag = 0
            url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
            response = urllib2.urlopen(url)
            html = response.read()news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:15]:
                sofiaResponse(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
            soup1 = soup(html,"lxml")
            url_list = []
            for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                    flag = 1
                    final_url = 'https://www.youtube.com' + vid['href']
                    url_list.append(final_url)
                    url = url_list[0]
                    ydl_opts = {}
                    os.chdir(path)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                        vlc.play(path)
                    if flag == 0:
                        sofiaResponse('I have not found anything in Youtube ')