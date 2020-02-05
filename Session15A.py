name = "John"
phone = "+91 98760 73031"
address = "Redwood Shores"

# file = open("data.csv", "w")
file = open("data.csv", "a")
data = "{},{},{}\n".format(name, phone, address)
print(data)
file.write(data)
file.close()

print(">> Data Saved in File")