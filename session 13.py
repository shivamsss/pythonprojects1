class Gaana:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def show(self):
        print("==========================================================")
        print("{}\t{}\t{}\t".format(self.title,self.artist,self.duration))



song1 = Gaana("Tum hi ho","Arijit",3.43)
song2 = Gaana("Befikre","Sonu Nigam",2.13)
song3 = Gaana("Ek Kuddi","Diljit",1.49)
song4 = Gaana("Desi Kalakar","Honey Singh",4.60)

song1.nextsong = song2
song2.nextsong = song3
song3.nextsong = song4

song2.prevsong = song1
song3.prevsong = song2
song4.prevsong = song3

current_song = song1
while current_song!= song4:
    current_song.show()
    current_song = current_song.nextsong

current_song.show()
# lastsong = current_song.nextsong
#
# lastsong.show()
