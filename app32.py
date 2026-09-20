# import json
# The json module is used to work with JSON data in Python.
# JSON (JavaScript Object Notation) is a common format for storing and exchanging data.
# It can convert Python objects into JSON strings and back again.

import json

# Example 1: Convert Python dictionary to JSON string
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(person)
print("JSON string:", json_string)

# Example 2: Convert JSON string back to Python dictionary
parsed_person = json.loads(json_string)
print("Python dictionary:", parsed_person)
print("Name:", parsed_person["name"])

# Example 3: Write JSON to a file
with open("person.json", "w") as file:
    json.dump(person, file)

# Example 4: Read JSON from a file
with open("person.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded from file:", loaded_data)

# Summary:
# json.dumps() -> Python object to JSON string
# json.loads() -> JSON string to Python object
# json.dump()  -> Python object to JSON file
# json.load()  -> JSON file to Python object
