# Dictionary example using keys(), values(), and items() methods
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Using keys() method       
print(f"Keys: {my_dict.keys()}")  # Output: Keys: dict_keys(['a', 'b', 'c'])

# The values() method returns a view object that displays a list of all the values in the dictionary.
print(f"Values: {my_dict.values()}")  # Output: Values: dict_values([1, 2, 3])

# The items() method returns a view object that displays a list of all the key-value pairs in the dictionary.
print(f"Items: {my_dict.items()}")  # Output: Items: dict_items([('a', 1), ('b', 2), ('c', 3)])         
