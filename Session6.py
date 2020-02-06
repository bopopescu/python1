#for i in range (1, 11):
#for i in range (1, 11,2):
for i in range (10, 0, -1):
     print(">> i is:", i)

print("==========")

"""
   show(num)  => print num
   
"""
#creating or defining a function
#recursion -> executing same fnc again nd again from the same function
def show(num):

    if num== 0:
        return                #return statement is an acknowledgement

    print(">> num is:", num)
    num -= 1  # num = num-1
    show(num)

#executing a function
show(10)
#show(9)
#show(8)
#show(7)
#show(6)
#show(5)

#running time of loop nd recursive fnc is same or different
#if same or more thn whts the fun? why we need it or use it!