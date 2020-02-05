salutation = "Mr."
fname = "George"

name = salutation + fname
print(">> name:", name)
print(">> salutation:", salutation)

num = "100"
print(">> num:", num, type(num))
print(">> is digit:", num.isdigit())

# num.  --> explore more is functions in string

songName= "Hello.mp3"
# starts with
if songName.endswith(".mp3"):
    print(">> We can play this audio file")
else:
    print(">> Invalid audio format")

# strings have so many buiolt in functions we need to explore them !!