# Types of Inheritance

"""
    1. Single Level
    A
    |
    B

    class A:
    pass

    class B:
    pass


    2. Multi-level
    A
    |
    B
    |
    C

    class A:
    pass

    class B(A):
    pass

    class C(B):
    pass

    3. Hierarchy
        A
       |
    B    C
     class A:
    pass

    class B(A):
    pass

    class C(A):
    pass

    4. Multiple
    A    B
       |
       C

    class A:
    pass

    class B(A):
    pass

    class C(A,B):
    pass

    5. Hybrid
      Any combination of above

"""


class A:

    a = 10

    def __init__(self, b):
        print(">> Object Constructed init of A:")
        self.b = b

    def show(self):
         print(">>a is:",  A.a)
         print(">>b is:", self.b)


class B:

    x = 10

    def __init__(self, y):
        print(">> Object Constructed init of B:")
        self.y = y

    def show(self):
        print(">>x is:", B.x)
        print(">>y is:", self.y)


class C(A, B):
    pass


cRef = C(10)
print(cRef.__dict__)

cRef.show()





