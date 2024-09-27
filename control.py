# control flows (if-else, for-loop, while-loop)
age = 20

if age < 18:
    print("Sorry, unable to join the part time class")
elif age > 60:
    print("Go home")
else:
    print("Get in class and start reading")

# loop through scores and print each value
scores = [79, 25, 40, 88]

for x in scores:
    print(x)

# while loop
i = 0
while i < len(scores):
    print(i)
    i += 1