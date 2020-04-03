import os

def play (text):
    return os.system("rhythmbox-client --play")
def pause (text):
    return os.system("rhythmbox-client --pause")
def next (text):
    return os.system("rhythmbox-client --next")
def prev(text):
    return os.system("rhythmbox-client --previous")
def printplay (text):
    return os.system("rhythmbox-client --print-play")
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