# Errors Generated at run time are called run time error : expections
# Exceptions are no good for our programs :(
# It will hamper performance of OS

print("-------------------------")
print(">> APP Started :)")
print("-------------------------")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

idx = int(input("Enter Your Lucky Number:"))
try:
    print("You Won Prize Of:", numbers[idx])  # After this line in try nothing will be executed
    print(">>Tjis is Awesome !!")
    print(">> Please enter your bank details to send money :)")

except Exception as e:
    print(">>Some Error:", e)



finally:
    print("Thanks for playing game")


"""
except IndexError as idxErr:
    print(">>Some Error:", idxErr)

except ZeroDivisionError as zdxErr:
    print(">>Some Error:", zdxErr)
"""


print("-------------------------")
print(">> APP Finished :)")
print("-------------------------")
