def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, name="John", email="john@example.com")


# error
# def fun(**kwargs,*args):
   # print(kwargs)
   # print(args)
# fun(10, 20, name="John", email="john@example.com")


