# BUILT in APIs i.e. FUNCTIONS

# strings are immutable
name = "Fionna Flynn"
print(">> name is:", name)
# maqnipulation oprtions will create a new string in memory, old string will cannot be modified
newName = name.upper()
print(">> newName is:", newName)

authorName = "john watson"
authorName = authorName.capitalize()
# we are creating a new string and refrencing it in our old ref value
print(">> authorName is:", authorName)

authorName = authorName.capitalize()
print(authorName, hex(id(authorName)))


names = "John, Jennie, Jim, Jack, Joe"
print(names[0])
print(names[len(names)-1])
idx = names.index("Jennie")
print(idx)

newNames = names.replace('J', 'K')
print(names)
print(newNames)

num = names.count("J", 0, len(names))
print(">> num is:", num)



quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
"""

def count(data,word, start, end):
    c = 0
    j = 0

    for i in range(start, end):
       if data[i] == word[0]:
           print(data[i] == word[j])
         # j+= 1





    return c

print(">> the occurs:", count(quotes,"the", 0, len(quotes)))