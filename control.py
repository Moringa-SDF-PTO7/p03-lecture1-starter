# control.py

# Conditional statements
age = 20
if age >= 18:
    print("You're an adult!")
else:
    print("You're not an adult yet.")

# TODO: Add an example using elif to check multiple conditions

# Loops
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# TODO: Write a while loop that continues until a variable reaches a certain value

# Decorators
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

# TODO: Create a new decorator that takes an argument and apply it to a function
