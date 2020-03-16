from Session32 import HashTable
# from Session32(i) import HashTable


class Student:

    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age= age

    def __str__(self):
        return "{}\t{}\t{}\t".format(self.roll, self.name, self.age)

s1 = Student(101, "John", 22)
s2 = Student(102, "Fionna", 24)
s3 = Student(103, "Jim", 27)
s4 = Student(104, "Jack", 25)
s5 = Student(105, "Dev", 21)

print(id(s1))

hTable = HashTable()
hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)

hTable.iterate()
