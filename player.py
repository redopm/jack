import os


class Player():
    def __init__(self, play, pause, next, previous, volume_up, volume_down, shuffle, no_shuffle, repeat, no_repeat):
        self.play = play
        self.pause = pause
        self.next = next
        self.previous = previous
        self.volume_up = volume_down
        self.volume_down =  volume_down
        self.shuffle = shuffle
        self.no_shuffle = no_shuffle
        self.repeat = repeat
        self.no_repeat = no_repeat

    def PLAY(self, text):
        os.system("rhythmbox-client --play")
        return 
    def PAUSE(self, text):
        os.system("rhythmbox-client --pause")
    def NEXT(self, text):
        os.system("rhythmbox-client --next")
    def PREV(self, text):
        os.system("rhythmbox-client --previous")
    def QUIT(self, text):
        os.system("rhythmbox-client --quit")
    def VOL_UP(self, text):
        os.system("rhythmbox-client --volume-up")
    def VOL_DOWN(self, text):
        os.system("rhythmbox-client --volume-down")
    def print_vol(self, text):
        os.system("rhythmbox-client --print-volume")
    def REP(self, text):
        os.system("rhythmbox-client --repeat")
    def NO_REP(self, text):
        os.system("rhythmbox-client --no-repeat")
    def SHUF(self, text):
        os.system("rhythmbox-client --shuffle")
    def NO_SHUF(self, text):
        os.system("rhythmbox-client --no-shuffle")       

