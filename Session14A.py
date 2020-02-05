# What is INHERITANCE ?
# It is a relationship between 2 classes,
# where child class is allowed to access properties of parent class


class Parent:

    # Property of class
    vehcile = "PB10AB1234"

    def __init__(self, fname, lname, wealth):
        self.fname = fname
        self.lname = lname
        self.wealth = wealth

# Inheritance


class Child(Parent):
    pass


"""

pRef = Parent("John", "Watson", 10000)
print("pRef Dictionary")
print(pRef.__dict__)

print("Parent Dictionary")
print(Parent.__dict__)

"""

print("Parent Dictionary")
print(Parent.__dict__)

print("Child Dictionary")
print(Child.__dict__)

# Object of Child
cRef = Child("Fionna", "Flynn", 150000)
print(">> Dictionary of cRef:")
print(cRef.__dict__)

# print(Child.vehcile)
print(cRef.vehcile)

