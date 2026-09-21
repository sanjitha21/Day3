#  Positional arguments

def add(a, b):
    return a + b
print("1. Positional arguments:", add(10, 20))

# Keyword arguments

def greet(name, message):
    return f"{message}, {name}!"
print("2. Keyword arguments:", greet(name="Alice", message="Hello"))

# Default arguments
def student(name, course="Python"):
    return f"{name} is learning {course}"

print("3. Default arguments:", student("Rahul"))
print("3. Default arguments with override:", student("Rahul", "Java"))

# 4. Variable-length arguments
def info(name, *skills, **details):
    print(f"Name: {name}")
    print(f"Skills: {skills}")
    print(f"Details: {details}")

print("4. Variable-length arguments:")
info("Sam", "Python", "AI", "ML", city="Delhi", age=25)


