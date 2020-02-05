def add(num1, num2):
    sum = num1 + num2
    print(">>Sum is{}".format(sum))


print(">> add is:",add)


#Re-Defining


def add(num1,num2, num3):
    sum = num1 + num2 + num3
    print(">> Sum is {}".format(sum))

print(">> add now is:",add)

#add (10,20) #error
add(10, 20, 30)