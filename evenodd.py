
def is_even(number):
  return number % 2 == 0

def is_odd(number):
  return not is_even(number)

def main():
  number = int(input("Enter a number: "))

  if is_even(number):
    print(number, "is even.")
  else:
    print(number, "is odd.")

main()