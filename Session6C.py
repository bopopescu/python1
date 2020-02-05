#passing references  |we understanding it as a value
def square(num):
    print(">>[SQUARE] num is:", num, hex(id(num)))    #num is reference variable which holds hashcode of 10
    num = num * num
    print(">>[SQUARE] num now is:", num, hex(id(num)))

num = 10   #num is reference variable which holds hashcode of 10
print(">>[MAIN]  num is:", num, hex(id(num)))

square(num)
print(">>[MAIN]  num now is:", num, hex(id(num)))

