# dict of list
student = {
    "name": ["Alice", "Bob", "Charlie"],
    "marks": [90, 85, 88],
    "subjects": ["Math", "Science", "English"]
}

print(student)

print(student["name"])
print(student["marks"][0])
print(student["subjects"][2])

#dict of tuple
# dict of tuple

student = {
    "name": ("Alice", "Bob", "Charlie"),
    "marks": (90, 85, 88),
    "subjects": ("Math", "Science", "English")
}

print(student)

print(student["name"])
print(student["marks"][0])
print(student["subjects"][2])

#dict of dict
# dict of dict

student = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "marks": 90
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "marks": 85
    }
}

print(student)

print(student["student1"])
print(student["student1"]["name"])
print(student["student2"]["marks"])