"""
     OOPS:  HAS-A Relationship


    1. Think of an Object

     Restaurant : name, phone, email, address, pricePerPerson, openingHours
     Menu       : name, description
     Dish       : name, price, description, type

     In Case for my Software we have many objects, we MUST have identify relationships between them

     1 to 1 Relationship
     -------------------
     1 Restaurant has 1 Menu


     1 to many Relationship
     ----------------------
     1 Restaurant has 2 Menus
     1 Menu has many Dishes

     many to many Relationship
     --------------------------
     Many Restaurant which can have Many Menus

      Restaurant : name, phone, email, address, pricePerPerson, openingHours, menu
     Menu       : name, description, dishes
     Dish       : name, price, description, type


"""
# 2. Create classes for object
class Restaurant:
    def __init__(self, name, phone, email, address, pricePerPerson, openingHours, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self. pricePerPerson = pricePerPerson
        self.openingHours = openingHours
        self.menu = menu

    def showRestaurant(self):
        pass

class Menu:

    def __init__(self, name , description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes

    def showMenu(self):
        pass

class Dish:

    def __init__(self, name, price, description, type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type

    def showDish(self):
        pass

# from class create real objects in memory
dish1 = Dish("Dal Makhani", 200, "Black Lentils Cooked Overnight", "Indian Veg")
dish2 = Dish("Panner Makhani", 300, "MakhanWala Panner", "Indian Veg")
dish3 = Dish("Burger", 200, "tikkiwala Burger", "Chinese")
dish4 = Dish("Noodles", 200, "Desi Noodles", "Chinese")
dish5 = Dish("Manchurian", 200, "Gol Gol Manchhurian", "Chinese")

# List Of Objects
dishes = [dish1, dish2, dish3, dish4, dish5]

# Menu Object Construction
menu = Menu("Sadabahar Menu", "All Indian and Chinese in Short",
            [
                 Dish("Dal Makhani", 200, "Black Lentils Cooked Overnight", "Indian Veg")
                 Dish("Panner Makhani", 300, "MakhanWala Panner", "Indian Veg")
                 Dish("Burger", 200, "tikkiwala Burger", "Chinese")
                 Dish("Noodles", 200, "Desi Noodles", "Chinese")
                 Dish("Manchurian", 200, "Gol Gol Manchhurian", "Chinese")
            ]
            )

