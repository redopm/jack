import os


class Player():
    def __init__(self, play, pause, next, previous, volume_up, volume_down, shuffle, no_shuffle, repeat, no_repeat, print_play):
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
        self.print_play = print_play

    def is_playing(self, text):
        '''Returns True if a song is being played'''
        if self.print_play():
            status = self.play
            return status == "Playing"
        else:
            return status =="Pause"
        return False

    def played(self, text):
        if self.pause == False:
            status = os.system("rhythmbox-client --play")
            return status == "playing"
        return False

    def PAUSED(self, text):
        return os.system("rhythmbox-client --pause")
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
    def REP(self, text):
        os.system("rhythmbox-client --repeat")
    def NO_REP(self, text):
        os.system("rhythmbox-client --no-repeat")
    def SHUF(self, text):
        os.system("rhythmbox-client --shuffle")
    def NO_SHUF(self, text):
        os.system("rhythmbox-client --no-shuffle")       

