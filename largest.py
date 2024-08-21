a=int(input(print("enter first number: ")))
b=int(input(print("enter second number: ")))
c=int(input(print("enter third number: ")))

find_max = lambda a, b, c: max(a, b, c)

result = find_max(a,b,c)
 
print("Maximum Number :", result)