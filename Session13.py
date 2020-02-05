# Principle of

# 1. Think of an object
#          Song : title, artist, duration
# 2. Write its Class

class Song:
    def __init__(self, title,artist, duration):
        # LHS: self. title is property of object
        # RHS: title is input to __init__
        self.title = title
        self.artist = artist
        self.duration = duration

    def showSongDetails(self):
        print(self.title, self.artist, self.duration)


song1 = Song("1. Muqabla", "Yash", 2.56)
song2 = Song("2. Ek Toh", "Neha  Kakkar", 3.44)
song3 = Song("3. Mubarqan", "Juggy", 5.50)
song4 = Song("4. Nai Jeena", "Yash", 9.75)
song5 = Song("5. Gulabi 2.0", "Ammal", 3.37)

print(">> song1 is:", song1)
print(">> song2 is:", song2)
print(">> song3 is:", song3)
print(">> song4 is:", song4)
print(">> song5 is:", song5)

# Reference Copy Operation
song1.nextSong = song2
song2.nextSong = song3
song3.nextSong = song4
song4.nextSong = song5
song5.nextSong = song1

# Reverse
song1.previousSong = song5
song2.previousSong = song3
song3.previousSong = song2
song4.previousSong = song1
song5.previousSong = song4

song1.showSongDetails()
song1.nextSong.showSongDetails()
song1.previousSong.showSongDetails()

start = song1

while start.nextSong != song1:
    print("-----------------")
    start.showSongDetails()
    print("-----------------")
    start = start.nextSong

# Sowing the last song details
start.showSongDetails()
print("-----------------")

print("^^^^^^^^Iterating Backward^^^^^^^")
current = song5

while current.previousSong != song5:
    print("*****************")
    current.showSongDetails()
    print("*****************")
    current =current.previousSong


current.showSongDetails()
print("*****************")




