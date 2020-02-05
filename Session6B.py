#print(__name__)

def sqaure():
    num = 20
    print(">> num in sqaure is:", num)
    sqaure()

def main():
    num = 10
    print(">> num in main is:", num)

    sqaure()
    print(">> This is main's last statement")
# if __name__ == "__main__":
#    main()