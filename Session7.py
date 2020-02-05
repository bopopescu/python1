"""
    Sequences in python
    Sequence : data with quite similar type

    Sequences listed below is also known as
    Built In Data Structures here in python

    Why data should be structured?
    1. Sort
    2. Search
    3. Filter

    please see:
    Tuple
   1. List
   2. String
   3. Set
   4. Dictionary

    Operations on sequences:
    1. Concatenation
    2. Repetition
    3. Membership training
    4. Slicing
    5. Indexing
"""

students = ("John", "Jennie", "Jim", "Jack", "Joe")
print(students)
print(type(students))

# 1. Concatenation | IMMUTABLE
newStudents = students + ("Fionna", "George")

print(newStudents)
print(students)

print()

# 2. Repetition
print(students*2)

print()

#3. Membership Training
print("John" in students)
print("Dev" not in students)

#4. Indexing
print(students[0])
print(students[len(students)-1])

#5. Slicing
print(students[0:2])
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)

# basic for loop
#for i in range(0, len(students))
#   print(students[i])

#enhanced version of for loop  | for each loop
for student in students:
   print(student)