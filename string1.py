def string_methods_demo(text):

  # Basic operations
  print("Length:", len(text))
  print("Uppercase:", text.upper())
  print("Lowercase:", text.lower())
  print("Capitalized:", text.capitalize())
  print("Title case:", text.title())
  print("Swapcase:", text.swapcase())

  # Checking properties
  print("Is alphanumeric:", text.isalnum())
  print("Is alphabetic:", text.isalpha())
  print("Is digit:", text.isdigit())
  print("Is lower:", text.islower())
  print("Is upper:", text.isupper())
  print("Is title:", text.istitle())
  print("Is space:", text.isspace())

  # Searching and finding
  print("Find 'world':", text.find("world"))
  print("Index of 'world':", text.index("world"))
  print("Starts with 'Hello':", text.startswith("Hello"))
  print("Ends with 'world!':", text.endswith("world!"))

  # Modifying strings
  print("Replace 'world' with 'Python':", text.replace("world", "Python"))
  print("Strip leading and trailing whitespace:", text.strip())
  print("Left justified (width 20):", text.ljust(20, '*'))
  print("Right justified (width 20):", text.rjust(20, '*'))
  print("Centered (width 20):", text.center(20, '*'))

  # Splitting and joining
  words = text.split()
  print("Split into words:", words)
  print("Joined with '-':", '-'.join(words))

  # Other methods (example)
  print("Count 'o':", text.count('o'))
  print("Partition at ',':", text.partition(','))

# Example usage
text = "  Hello, world!  "
string_methods_demo(text)
