import pandas as pd
import numpy as np

oddNumbers = np.arange(1, 100, 2)
evenNumbers = np.arange(0, 100, 2)


numbers = {"oddNumbers": oddNumbers, "evenNumbers": evenNumbers}

table = pd.DataFrame(numbers)
print(table)

print("**********")

print(table.sum())

print("**********")


print(table.max())

print("**********")

print(table.min())

print("**********")

