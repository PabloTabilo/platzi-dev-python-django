import random
from node_based_queue import Queue

class MusicPlayer():
    def __init__(self):
        self.q = Queue()

    def addSong(self, song):
        self.q.enqueue(song)

    def playSong(self):
        print(f"Listen {self.q.head.data}")
        return self.q.dequeue()

    def getSongs(self):
        print(self.q.__str__())

def main():
    playList = MusicPlayer()
    playList.addSong("Time to pretend")
    playList.addSong("Radio Head")
    playList.addSong("Metallica")
    playList.getSongs()
    playList.playSong()
    playList.getSongs()

if __name__ == '__main__':
    main()