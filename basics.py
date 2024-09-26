# basics.py

# Debugging with ipdb
import ipdb

def buggy_function():
    x = 5
    y = 0
    ipdb.set_trace()  # Debugging here
    z = x / y  # Will raise a ZeroDivisionError
    return z

# TODO: Uncomment and run buggy_function to observe debugging in action.
# buggy_function()

# Testing with pytest
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

# TODO: Add more tests with pytest to cover subtraction, multiplication, etc.

# Indentation and variable scope
def outer_function():
    x = 10  # Outer function scope
    
    def inner_function():
        nonlocal x  # Referencing variable from outer scope
        x += 5
        print(f"Inner function, x = {x}")
    
    inner_function()
    print(f"Outer function, x = {x}")

outer_function()

# TODO: Add more examples to explain local, global, and nonlocal scope
