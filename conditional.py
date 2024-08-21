
x = 5
y = 10
z = 15

# If statement
if x > 10:
    print("x is greater than 10")
print("End of if statement")

# If-else statement
if y > 15:
    print("y is greater than 15")
else:
    print("y is less than or equal to 15")
print("End of if-else statement")

# If-elif-else statement
if z > 20:
    print("z is greater than 20")
elif z == 15:
    print("z is equal to 15")
else:
    print("z is less than 15")
print("End of if-elif-else statement")

# Nested if-else statement
if x > 5:
    if y > 10:
        print("x is greater than 5 and y is greater than 10")
    else:
        print("x is greater than 5 but y is not greater than 10")
else:
    print("x is not greater than 5")
print("End of nested if-else statement")

