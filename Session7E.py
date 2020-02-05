data = [1, 2, 3, 4, 5]
print(len(data))
print(max(data))
print(min(data))

#hw: You code ypour own functions

def myLen(data):
    length = 0
    return length

def myMax(data):
    length = 0
    return max

def myMin(data):
    length = 0
    return min

# List Comprehensive
print([x**2 for x in data])

productPrices = [1123, 1342, 3341, 4421, 5456]
print([0.4*x for x in productPrices])

# list comprehensive and expressions: error
# explore do we have any other way to do the same

numbers = list(range(1, 101))
print(numbers)

names1 = ("John", "Jennie", "Jim", "John", "Jack")
names2 = list(names1)
names3 = set(names1)
#names4 = dic(names1)