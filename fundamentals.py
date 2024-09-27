# Data Types
age = 32                    #integer
height = 130.5              #float
isOld = True                #Boolean (True/False)
first_name = "Alex"         #string
scores = [79, 25, "40", 88] #list (mutable in nature => value can change)
names = ("Daniel", "Shanice") # tuple (immutable in nature => values can never change)
student = { "name" : "Gloria", "email" : "gloria@mail.com" } #Dictionary
heights = { 178, 192, 188, 178, 192, 200, 109, 77 } # set (unique values ~ not have an order)

print(heights)
 
## list
firstItem = scores[0]  # indexing starts from 0 in python
scores[2] = 99         # Change values in a list


## tuple
firstTupleItem = names[0] # get a value at a specific index

# try ... except
try:
    results = 10 / 0
    # stuff goin on here
except ZeroDivisionError as e:
    print("An error occurred: " + str(e))

try:
    print(abc)
except:
    print("A general error occurred")

# TODO: Write a try-except block for handling both ValueError and TypeError