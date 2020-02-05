# 1. Think of an object
#     Customer is object
#     name,phone,email,gender,address are attributes

class Customer:
    pass
cRef1 = Customer()  # Object Construction Statement
cRef2 = Customer()  # Object Construction Statement
cRef3 = cRef1       # Reference Copy Operation


print(">> cRef1 is:", cRef1)
print(">> cRef2 is:", cRef2)
print(">> cRef3 is:", cRef3)

# Operations on object
# 1. Add data in object

cRef1.name = "John"
cRef3.phone = "+91 98765 43210"
cRef1.email = "john@example.com"
cRef1.gender = "Male"
cRef1.address = "Redwood Shores"

cRef2.name = "Fionna"
cRef2.phone = "+91 98765 01234"
cRef2.email = "fionna@example.com"
cRef2.gender = "Female"
cRef2.vehicle = "KA10AB3456"
cRef2.address = "Country Homes"
cRef2.company = "ABC International"

# 2. Read Data from object
print(">> cRef1 Details:")
print(cRef1.__dict__)
print()

print(">> cRef2 Details:")
print(cRef2.__dict__)
print()

print(">> cRef3 Details:")
print(cRef3.__dict__)
print()

# For end User
print(">> {} can be called at {} and lives {}".format(cRef3.name, cRef1.phone, cRef3.address))
print(">> {} can be called at {} and lives {}".format(cRef2.name, cRef2.phone, cRef2.address))

# 3. Update Data in Object
cRef1.name = "John Watson"
cRef3.email = "watson@example.com"

cRef2.name = "Fionna Flynn"
cRef2.phone = "+91 98752 31254"

print("===Details Updated===")

print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef3.name, cRef1.phone, cRef3.address))
print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef2.name, cRef2.phone, cRef2.address))

# 4. Delete Data in object

del cRef1.email
del cRef2.vehicle

print(">> cRef1:", cRef1)
print(">> cRef2:", cRef2)
