"""
       Class : Attributes and methods / functions
               whatever u write in class belongs to class
               it is also a multi value container
               whatever is in the class  is common for all its objects


       Object: Attributes will be created with self

"""
# WhatsAppGroup --> title
class WhatsAppGroup:

    title = "PropertyOfObject"
    image = "abc.jpg"

    def show(self):
        print(">> title is:", self.title)
        print(">> image is:", self.image)



group = WhatsAppGroup()
print(">> Dictionary of group is :")
print(group.__dict__)
print()

class Counter:

    # Property of class
    sCount = 1

    def __init__(self):
        self.count = 1

    def increment(self):
        self.count += 1
        # self.sCount += 1  # --> self.sCount = self.sCount + 1
        Counter.sCount += 1


    def decrement(self):
        self.count -= 1
        # self.sCount -= 1
        Counter.sCount -= 1

    def showCount(self):
        print(">> count is: {} and sCount is: {}".format(self.count, Counter.sCount))

c1 = Counter()
c2 = Counter()
c3 = c1

c1.increment()
c1.increment()
c2.increment()
c3.increment()

c1.decrement()
c3.increment()
c2.increment()

c1.showCount()
c2.showCount()
c3.showCount()




