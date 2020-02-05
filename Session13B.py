class Product:

    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.nextProduct= None
        self.prevProduct = None
        self.quantity = 0


    def showProductDetails(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}\t{}\t".format(self.pid, self.name, self.price))
        print("~~~~~~~~~~~~~~~~~~~~~~~")

class LinkedList:

    def __init__(self):
        print(">> Linked List Created")
        print(self)
        self.head = None
        self.current = None

    def append(self, product):
        print(product)
        LinkedList.size += 1
        LinkedList.items += product.quantity
        LinkedList.price += (product.quantity * product.price)

        if self.head == None:
            self.head = product
            self.current = product

        else:
            product.prevProduct =



