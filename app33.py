# Sets in Python

numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", numbers)

fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)


print("Is 'apple' in fruits?", "apple" in fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

# Converting a list to a set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = set(my_list)
print("List converted to set:", unique_list)


