names = "John, Jennie, Jim, Jack, Joe"
splittedNames = names.split(",")
print(splittedNames, type(splittedNames))

for name in splittedNames:
    print(name.strip())

quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
"""

words = quotes.split(" ")
print(words)
for word in words:
    print(word)


# hw:
def split(sentence):

    words=[]

    return words

split("Search the Candle, rather than cursing the darkness")