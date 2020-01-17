#container creation statement
# single value container
number = 10

#multi value container
numbers = 10, 20, 30, 40, 50
#numbers = (10, 20, 30, 40, 50)
#we can write numbers in () brackets


#read/print statement
print("number:", number, type(number), id(number))
print("numbers:", numbers, type(numbers), id(numbers))

print("numbers[0]:", numbers[0], type(numbers[0]), id(numbers[0]))
print("numbers[1]:", numbers[1], type(numbers[1]), id(numbers[1]))
print("numbers[2]:", numbers[2], type(numbers[2]), id(numbers[2]))
print("numbers[3]:", numbers[3], type(numbers[3]), id(numbers[3]))
print("numbers[4]:", numbers[4], type(numbers[4]), id(numbers[4]))

#PS: number and numbers are reference variables
#    they
#
#    rather we see the data. this is MAGIC
age= 30
print("agae:", age, type(age), id(age))

#del age
#print("age after we have deleted age:", age)
#print("numbers[2] after we deleted age:", numbers[2])
#these 2 lines will not run because of wrong statements