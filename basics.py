# Tests using pytest
def sum(a, b):
    return a + b


## simple test
def sumTest():
    print("we are inside sumTest")
    assert sum(2, 5) == 7
results = 23 / 10
print(results)


## run test
sumTest()