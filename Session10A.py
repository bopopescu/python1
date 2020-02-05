# variable arguments in python
def add(*args):
    print(args)
    print(type(args))

    sum = 0
    for data in args:
        sum = sum + data
    print(">> sum is :")


add(10,20)
add(10, 20, 30, 40, 50)
add(10, 20, 30, 11, 134, 135, 678)

def addAgain(numbers):
    sum = 0
    for data in numbers:
        sum = sum + data
    print(">> sum is :")

data = (10, 20, 30, 40, 50)

