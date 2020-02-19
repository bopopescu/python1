import numpy as np

numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

print()

# numpy array is optimised as a compared to the list :)

array = np.array(numbers)
print(array, type(array))

# Explore with string, tuple, set and dictionary
array1 = np.array((10, 20,30, 40, 50))
print(array1, type(array1))
print()

array2 = np.array({10, 20,30, 40, 50})
print(array2, type(array2))
print()

array3 = np.array("Hello")
print(array3, type(array3))
print()

array4 = np.array({"name": "John", "age": 30})
print(array4, type(array4))
print()

array5 = np.array(30)
print(array5, type(array5))
print()


# Updating data in numpy
array1[2] = 222
print(array1)

# Iterate in numpy array

"""
for i in range(0, len(array1)):
    print(array1)

"""


for num in array1:
    print(num)

print()

#
array = np.append(array1, [11, 22, 33, 44, 55])
print(array1)
print(array)