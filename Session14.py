class CA:

    # In Python, Overloading is not SUPPORTED
    def __init__(self):
                 # If you re-define previous functions again
        print(">>CA Object Constructed")

    def __int__(self,num ):
        print(">> new CA Object Constructed")

cRef = CA()

# So, we need to maintain standardization while creating Objects