# explain tuple of list with example
# explain tuple of list wu

my_tuple = ([1, 2], [3, 4], [5, 6])

print("Tuple of lists:")
print(my_tuple)

print("\nFirst list:")
print(my_tuple[0])

print("\nSecond item of first list:")
print(my_tuple[0][1])

#tuple of tuple
my_tuple = ((1, 2), (3, 4), (5, 6))

print("Tuple of tuples:")
print(my_tuple)

print("\nFirst tuple:")
print(my_tuple[0])

print("\nSecond item of first tuple:")
print(my_tuple[0][1])

#tuple of dict
# explain tuple of dict with example

my_tuple = (
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30}
)

print("Tuple of dictionaries:")
print(my_tuple)

print("\nFirst dictionary:")
print(my_tuple[0])

print("\nName of first dictionary:")
print(my_tuple[0]["name"])