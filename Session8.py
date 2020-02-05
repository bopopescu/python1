"""

     String     #can write string in single quote ' '
     Set
     Dictionary
"""

# johnsShop = 'Johns Coffee Shop'       #johnsShop ='John's Coffee Shop'  --> error .... to cover error we have to put \'s
# johnsShop = 'John\'s Coffee Shop'    #escape sequences [google it]
# johnsShop = "John's Coffee Shop"

# raw string [wescape sequences in a string]hich will ignore

johnsShop =r'John\'s Coffee Shop'
print(johnsShop, type(johnsShop))

# quote = "Work Hard, Get Luckier\n-Anonymous"
quote = r"Work Hard, Get Luckier\n-Anonymous"
print(quote)

message = "This is an Awesome Day" \
          "We will code together" \
          "Thank You :)"

print(message)

quotes = """Work Hard,Get Luckier
Search the Candle, rather than cursing the darkness
"""

print(quotes, type(quotes))

# search --> likewise we have put r in front of string what else we can put:))