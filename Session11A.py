# 1. Think of an object
#     Customer is object
#     name,phone,email,gender,address are attributes

# 2. Create its Class
class Customer:
    def __init__(self):
       print("init executed")
       print(">> self is:", self)
       self.name = "John"

# 3. From Class Create Real Object
cRef1 = Customer()     # Object Construction statement
print(">> cref1 is:", cRef1)
cRef1.phone = "+91 98745 65654"

print(cRef1.__dict__)

cRef2 = Customer()
cRef2.phone = "+91 98754 55555"

print(cRef2.__dict__)

# Refernce Copy Operation
cRef3 = cRef1