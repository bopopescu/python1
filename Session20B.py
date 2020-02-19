def hello():
    print("Hello..")

    # Nested Function or Inner Function
    def bye():
        print("Bye..")


    print(bye)
    bye()


print(hello)
hello()