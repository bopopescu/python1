name = "John Watson"
print(name, type(name),hex(id(name)))

# name is a reference variable which will hold hashcode of john watson
# john watson will be created in constant pool
print(">> Length of Name:", len(name)) # (0 to 10) # total length = 11 (0,1,2,3,4,5,6,7,8,9,10)
print(">> Max of Name:", max(name))    # t
print(">> Min of Name:", min(name))    # space

print(name[1])
print(name[len(name)- 1])

# string slicing
print(name[1:4])
# -ve indexing means reverse order
print(name[1], name[-2])

#reverse string
print(name[::-1])

email = input("Enter Your Email:")
print(">> You Entered:", email)


phone = input("Enter Your PhoneNum:")
print(">> You Entered:", phone)

if "@" in email and "." in email:
    print(">> Valid Email")
else:
    print(">> Invalid Email")

if len(phone) > 10 and len(phone) <= 15:
    print(">> Valid Phone")
else:
    print(">> InValid Phone")

