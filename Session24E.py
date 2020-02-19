import numpy as np
chessboard = np.zeros((8, 8), dtype=int)
print(chessboard)

# slicing and substituition
chessboard[1::2, 0::2] = 1
# chessboard[::2, 1::2] = 1

print(chessboard)

print("==========")

indexes = []

for i in range(0, len(chessboard)):
    print("Where Would You Like to Place Queen #{} eq:1,2".format(i+1))
    i = int(input("Enter Row Position: "))
    j = int(input("Enter Column Position: "))

    if (i>=0 and i<=7) and (j>=0 and j<=7):
        chessboard[i] [j] = 9
    else:
       print("Please Enter Correct Position :)")

    indexes.append([i, j])