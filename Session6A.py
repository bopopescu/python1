print(">> Welcome To Python App")

num = 5
print(">> 1. num is:", num)

def square(n):
    global num   #it means the num in line number 3
    n = n*n
    num = n
    print(">> 2. num is:", num)
    print(">> 3. num is:", num)
    #return -> last statement always means return



square(7)
print(">> 4. num is:", num)
