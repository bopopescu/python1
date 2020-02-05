"""

class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email ))

    def showPrimeCustomer(self):
        print("PRIME CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email, self.type))

cRef1 = Customer("John", "+91 98760 73031", "john@example.com")
cRef2 = Customer("fionna", "+91 99155 73031", "fionna@example.com")

cRef2.type = 1

print(cRef1.__dict__)
print(cRef2.__dict__)

cRef1.showCustomer()
cRef2.showCustomer()

cRef1.showPrimeCustomer()
cRef2.showPrimeCustomer()

"""

"""
class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("CUSTOMER: {} | {} | {}".format(self.name, self.phone, self.email ))

class PrimeCustomer(Customer):

     def upgradeToPrime(self, customer):
    # def __init__(self, customer):
        self.prime = True
        self.videos = True
        self.music = True

     def showPrimeCustomer(self):
        self.showCustomer()

        customerDetails = self.__dict__
        keys = customerDetails.keys()

        if "prime" in keys:
            print("PRIME FEATURES: VIDEOS: {} | MUSIC: {}".format(self.video, self.music))


cRef1 = Customer("John", "+91 98760 73031", "john@example.com")
cRef2 = Customer("fionna", "+91 99155 73031", "fionna@example.com")
print(cRef1.__dict__)

PrimeCustomer.upgradeToPrime(cRef1)
print(cRef1.__dict__)

PrimeCustomer.showCustomer(cRef1)
print()

PrimeCustomer.upgradeToPrime(cRef2)
PrimeCustomer.showPrimeCustomer(cRef2)

"""


class McdBurger:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def showMcdBurger(self):
            print("MCD BURGER: {} | {} | {}".format(self.name, self.price))


class HappyMeal(McdBurger):

    def upgradeToMeal(self):
        self.burger = True
        self.fries = True
        self.price = True

    def showHappyMeal(self):
        self.showMcdBurger()

        burgerrDetails = self.__dict__
        keys = burgerrDetails.keys()

        if "meal" in keys:
            print("HAPPY MEAL INCLUDES: BURGER: {} | FRIES: {} | PRICE: {}".format(self.burger, self.fries, self.price))


cRef1 = McdBurger("Burger", 50)
cRef2 = HappyMeal("AlloTikkiBurger", "French Fries", 250)
print(cRef1.__dict__)

HappyMeal.upgradeToMeal(cRef1)
print(cRef1.__dict__)

HappyMeal.showHappyMeal(cRef1)
print()

HappyMeal.upgradeToMeal(cRef2)
HappyMeal.showHappyMeal(cRef2)
