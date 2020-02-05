"""
    Types of Recursion:

     1.
     2.
     3. Tail Recursion
"""
def fun():

    fun()                #direct recursion


def fun1():

    fun2()


def fun2():

    fun1()

def fun3():

    fun1()

# def tailRec():

