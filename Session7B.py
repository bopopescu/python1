students = ["John", "Jennie", "Jim", "Jack", "Joe", ["Jim","Jack"]]
print(students, hex(id(students)))

newStudents = students + ["Fionna", "George"]
print(students, hex(id(newStudents)))

# Operation -> Concatenation in the same List
students = students + ["Fionna", "George"]
print(students, hex(id(students)))

someStudents = ["Jim","Joe"]
print(someStudents in newStudents)

someStudents = ["Jim","Jack"]     #to make it true we put list in list see line 1st
print(someStudents in newStudents)

