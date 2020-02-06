num1 = 10
print("num1:", num1, type(num1))

#tuple  : immutable
num2 = (10, 20, 30, 40, 50, 30)
print("num2:", num2, type(num2))

#list  : mutable
num3 = [10, 20, 30, 40, 50, 30]
print("num3:", num3, type(num3))

#set  :unique and mutable
num4 = {10, 20, 30, 40, 50, 30}
print("num4:", num4, type(num4))

#String  | IMMUTABLE
name = "John Watson"
print("name:", name, type(name))
#to achieve uniqueness set hashes the data and we don't have indexes
#due to hashing here in set output is unordered
print(num2[1])
print(num3[2])
#print(num4) #error

#num2[2] = 11 #error
num3[1] =11 #ok
#num4[1] = 11  #err
#name[1] = "k"  #err
print(name)

#DICTONARY : KEY AND VALUE PAIR  |MUTABLE
#On the web terminology  is JSON: JAVA SCRIPT OBJECT NOTATION

customer = {  "name": "John",
              "age": 30,
              "email": "John@example.com",
              "rating":4.5,
              "loyalitypoints":5133,
           }

customer["name"] ="John Watson"
customer["phone"] = "+91 9876543219"
print(customer, type(customer))
