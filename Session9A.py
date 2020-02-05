employee = {
    "name": "John",
    "eid": 101,
    "salary": 3000,
    "rating": 4.5,
}

print(employee, type(employee))
print(len(employee))
print(max(employee))
print(min(employee))

employee["name"] = "John Watson"

print(employee)

employee["address"] = "Redwood Shores"

print(employee)

# delete a key value pair
del employee["eid"]
print(employee)


keys = list(employee.keys())
values = list(employee.values())

print(">> keys is:", keys, type(keys))
print(">> values is:", values, type(values))