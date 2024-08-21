# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("End of for loop")

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
print("End of while loop")

# Nested loops
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")
print("End of nested loops")

# Break statement
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
print("End of break statement")

# Continue statement
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
print("End of continue statement")

# Pass statement
for fruit in fruits:
    if fruit == "banana":
        pass
    print(fruit)
print("End of pass statement")