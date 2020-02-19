#container creationer
num1 = 10

print("num1:", num1, id(num1))
#container creation with reference copy operation
num2 = num1
print("num2:", num2, id(num2))

#update operation
num1 = 100
print("num1 after updated:", num1, id(num1))


#container creation
#tuple: IMMUTABE | we cannot change it later
#numbers1 =10, 20, 30, 40, 50

#list: MUTABLE |we can change list later
numbers1 =[10, 20, 30, 40, 50]


#reference copy operation
numbers2 = numbers1

print("numbers1[2] is:", numbers1[2])
print("numbers2[2] is:", numbers2[2])

#update operation |for tupl(err) | fpr list0[work]
numbers1[2] = 33

print("numbers1[2] now is:", numbers1[2])
print("numbers2[2] now is:", numbers2[2])