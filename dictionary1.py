
dict = {"name": "Aarya", "age": 20, "city": "Kolhapur"}

# 1. clear()
print("Original dictionary: ", dict)
dict.clear()
print("Dictionary after clear(): ", dict)

dict = {"name": "Aarya", "age": 20, "city": "Kolhapur"}

# 2. copy()
dict_copy = dict.copy()
print("Original dictionary: ", dict)
print("Copied dictionary: ", dict_copy)

# 3. fromkeys() 
keys = ["a", "b", "c"]
value = 0
new_dict = dict.fromkeys(keys, value)
print("New dictionary: ", new_dict)

# 4. get() 
print("Value for 'name' key: ", dict.get("name"))

# 5. items() 
print("Dictionary items: ", dict.items())

# 6. keys() 
print("Dictionary keys: ", dict.keys())

# 7. pop()
print("Original dictionary: ", dict)
dict.pop("age")
print("Dictionary after pop(): ", dict)

# 8. popitem() 
print("Original dictionary: ", dict)
dict.popitem()
print("Dictionary after popitem(): ", dict)

# 9. setdefault() 
dict.setdefault("country", "USA")
print("Dictionary after setdefault(): ", dict)

# 10. update() 
dict.update({"language": "English", "hobby": "Reading"})
print("Dictionary after update(): ", dict)

# 11. values() 
print("Dictionary values: ", dict.values())