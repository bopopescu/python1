class Dish:

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.type = type
        self.quantity = 0

    def showDish(self):
        print("====={}====".format(self.name))
        print("{}\t{}\t{}\t{}".format(self.price, self.description, self.type, self.quantity))
        print("==============")


dish1 = Dish("Dal Makhani", 200, "Black Lentils Cooked Overnight", "Indian Veg")
dish2 = Dish("Panner Makhani", 300, "MakhanWala Panner", "Indian Veg")
dish3 = Dish("Burger", 200, "tikkiwala Burger", "Chinese")
dish4 = Dish("Noodles", 200, "Desi Noodles", "Chinese")
dish5 = Dish("Manchurian", 200, "Gol Gol Manchhurian", "Chinese")

cart = []
totalDishes = 0


def addDishToCart(dish):
    global totalDishes
    cart.append(dish)
    totalDishes += 1

dish1.quantity = 1
dish3.quantity = 3
dish4.quantity = 4


addDishToCart(dish1)
addDishToCart(dish3)
addDishToCart(dish4)

totalPrice = 0
totalItems = 0

for dish in cart:
    dish.showDish()
    totalPrice += (dish.price*dish.quantity)
    totalItems += dish.quantity

print(">> Total Prices:\u20b9", totalPrice)
print(">> Total Items:", totalItems)
print(">> Total Dishes:", totalDishes)