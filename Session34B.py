import pandas as pd
import numpy as np

data = np.random.randn(5, 4)
print(data)

table = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"])
print(table)

print("^^^^^^^^^^^^")

print(table["COL2"])

print("^^^^^^^^^^^^")

print("~~~~~~~~COL3 Data~~~~~~~~~~")

print(table.COL3)

print(">> Iterate in DataFrame")

for key, value in table.iteritems():
    print(key)
    print("^^^^^^^^^^^^")
    print(value)
    print("^^^^^^^^^^^^")

print()



