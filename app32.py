import json

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(person)
print("JSON string:", json_string)


parsed_person = json.loads(json_string)
print("Python dictionary:", parsed_person)
print("Name:", parsed_person["name"])


with open("person.json", "w") as file:
    json.dump(person, file)


with open("person.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded from file:", loaded_data)


