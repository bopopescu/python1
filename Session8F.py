S1 = {1, 2, 3, 4, 5}
S2 = { 3, 4, 5,6}

print(S1, type(S1))
print(S2, type(S2))

S3 = S1 | S2   # Union
print("Union:", S3)

S4 = S1 & S2   # Difference
print("Difference:",S4)

S5 = S1 - S2   # Intersection
print("Intersection:",S5)
