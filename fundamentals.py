# fundamentals.py

# Data types
integer = 42         # Integer
floating_point = 3.14 # Float
boolean = True       # Boolean
string = "Hello, World!" # String
list_example = [1, 2, 3, 4]  # List
tuple_example = (1, 2, 3)    # Tuple
dictionary = {'key': 'value'} # Dictionary

# TODO: Add more examples for other data types (e.g., sets, NoneType)

# Error messages
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

try:
    numbers = [1, 2, 3]
    print(numbers[5])  # This will raise an IndexError
except IndexError as e:
    print(f"Error occurred: {e}")

# TODO: Write a try-except block for handling ValueError and TypeError
