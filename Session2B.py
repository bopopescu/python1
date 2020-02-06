#single value container

#container creation statement
age = 20

#read/print statement
#type -> class
#id   ->hashcode
print("Age:",age, type(age), id(age))
print(age, type(age), hex(id(age)))
print(age, type(age), oct(id(age)))
print(age, type(age), bin(id(age)))

#container creation statement
johnsAge = 20
print("johnsAge:",age, type(johnsAge),id(johnsAge))

#container update statement
age = 30
print("Age:",age, type(age), id(age))
print(age, type(age), hex(id(age)))
print(age, type(age), oct(id(age)))
print(age, type(age), bin(id(age)))

#PS: Containers in memory are stored as data structure: hashtable with algorithm called hashing

fionnasAge = age       #copy operation or #reference copy operation
print("fionnasAge:",age, type(fionnasAge),id(fionnasAge))

#delete operation
del age
#print(age, type(age), (id(age)) #error
print("fionnasAge:", fionnasAge, type(fionnasAge), id(fionnasAge))

del fionnasAge

# PS:  age, johnsAge and fionnasAge are known as REFERENCE VARIABLES
# REFERENCE VARIABLES will hold HashCodes
