# 4 types of function calls with arguments in Python

# 1. Positional arguments
# The arguments are passed in the same order as the parameters.
def add(a, b):
    return a + b

print("1. Positional arguments:", add(10, 20))

# 2. Keyword arguments
# The arguments are passed by parameter name.
def greet(name, message):
    return f"{message}, {name}!"

print("2. Keyword arguments:", greet(name="Alice", message="Hello"))

# 3. Default arguments
# If no value is provided, the default value is used.
def student(name, course="Python"):
    return f"{name} is learning {course}"

print("3. Default arguments:", student("Rahul"))
print("3. Default arguments with override:", student("Rahul", "Java"))

# 4. Variable-length arguments
# *args: accepts multiple positional arguments
# **kwargs: accepts multiple keyword arguments

def info(name, *skills, **details):
    print(f"Name: {name}")
    print(f"Skills: {skills}")
    print(f"Details: {details}")

print("4. Variable-length arguments:")
info("Sam", "Python", "AI", "ML", city="Delhi", age=25)

# Summary:
# - Positional: add(10, 20)
# - Keyword: greet(name="Alice", message="Hello")
# - Default: student("Rahul")
# - Variable-length: info("Sam", "Python", "AI", city="Delhi")
