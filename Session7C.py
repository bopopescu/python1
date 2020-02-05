students = {"John", "Jennie", "Jim", "Jack", "Joe"}
print(students, hex(id(students)))
print(type(students))

newStudents = students + {"Fionna", "George"}
print(newStudents, hex(id(newStudents)))
print(type(newStudents))


# Operation -> Concatenation in the same List
students = students + {"Fionna", "George"}
print(students, hex(id(students)))
print(type(students))

someStudents = {"Jim","Joe"}
print(someStudents in newStudents)

