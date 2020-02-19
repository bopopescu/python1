def dataGenerator ():

    file = open("data.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line

result = dataGenerator()

print(result)
print(next(result))
print(next(result))