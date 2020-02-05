# What is INHERITANCE ?
# It is a relationship between 2 classes,
# where child class is allowed to access properties of parent class


class Parent:

    # Property of class
    vehcile = "PB10AB1234"

    # Property of Parent Class
    def __init__(self, fname, lname, wealth):
        # self.fname, self.lname, self.wealth is Property of Object

        self.fname = fname
        self.lname = lname
        self.wealth = wealth

    def showDetails(self):
        print("{}  |  {}  |  {}  |  {}  ".format(self.fname, self.lname, self.wealth, Parent.vehcile))


class Child(Parent):

    # Property of Child Class
    vehcile = "KA10XY3333"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        print("{}|{}|{}".format(self.name, self.salary, Child.vehcile))

    def show(self, ref):
        print("{}|{}|{}".format(self.name, self.salary, Child.vehcile))
        Parent.showDetails(ref)


cRef = Child("Fionna Flynn", 30000)
print(">> Dictionary of cRef:")
print(cRef.__dict__)


print(Child.vehcile)    # OK
print(cRef.vehcile)     # Ok


#cRef.showDetails()
Child.showDetails(cRef)

pRef = Parent("John", "Watson", 10000)
pRef.showDetails()

print("***********")

cRef.show(pRef)

# LOOKUP RULE :
# if we have not found an attribute in object, look up for
# in inheritance lookup shall go upto parent


