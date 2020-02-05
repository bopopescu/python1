# String Formatting

name = "Fionna"
age = 22

print(">> Welcome To our App", name)
print(">> Welcome To our App %s" % (name) )

print(">>" ,name, "Since you are", age, "years old. You can Vote")
print(">> {} Since you are {} years old. You can Vote".format(name, age))

message = "{} Since you are {} years old. You can Vote".format(name, age)

# SQL query
# sql = "insert into Customer values(1,'john', 'john@example.com')"

cid = int(input("Enter your Customer Id:"))
name = int(input("Enter your Name:"))
email = int(input("Enter your Email Id:"))

sql = "insert into Customer values({},'{}','{}')".format(cid, name, email)
print(">>SQL:", sql)


products = [3454, 2411,1341, 4568, 8967]
for i in range(0, len(products)):
    #products[i] = products[i] - (0.4*products[i])
    oldPrice = products[i]
