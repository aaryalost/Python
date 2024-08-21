
my_tuple = (1, 2, 3, 4, 5)

# 1. len() 
print("Length of the tuple: ", len(my_tuple))

# 2. max() 
print("Maximum value in the tuple: ", max(my_tuple))
print("Minimum value in the tuple: ", min(my_tuple))

# 4. tuple() 
my_list = [1, 2, 3, 4, 5]
my_tuple_from_list = tuple(my_list)
print("Tuple from list: ", my_tuple_from_list)

# 5. any() 
print("Any item in the tuple is true: ", any(my_tuple))

# 6. all() 
print("All items in the tuple are true: ", all(my_tuple))

# 7. enumerate() 
for i, value in enumerate(my_tuple):
    print("Index: ", i, " Value: ", value)

# 8. zip() 
my_tuple2 = (6, 7, 8, 9, 10)
zipped_tuple = zip(my_tuple, my_tuple2)
for item in zipped_tuple:
    print(item)

# 9. sorted() 
sorted_tuple = sorted(my_tuple)
print("Sorted tuple: ", sorted_tuple)

# 10. tuple.index() 
print("Index of 3 in the tuple: ", my_tuple.index(3))

# 11. tuple.count() 
print("Count of 3 in the tuple: ", my_tuple.count(3))

# 12. tuple.__add__() 
my_tuple3 = (11, 12, 13)
concatenated_tuple = my_tuple + my_tuple3
print("Concatenated tuple: ", concatenated_tuple)

# 13. tuple.__contains__() 
print("Is 3 in the tuple: ", 3 in my_tuple)

# 14. tuple.__getitem__() 
print("Item at index 2: ", my_tuple[2])

# 15. tuple.__iter__() 
iterator = iter(my_tuple)
for item in iterator:
    print(item)

# 16. tuple.__len__() 
print("Length of the tuple: ", my_tuple.__len__())

# 17. tuple.__mul__() 
repeated_tuple = my_tuple * 2
print("Repeated tuple: ", repeated_tuple)

# 18. tuple.__rmul__() 
repeated_tuple = 2 * my_tuple
print("Repeated tuple: ", repeated_tuple)

# 19. tuple.__repr__() 
print("Representation of the tuple: ", my_tuple.__repr__())

# 20. tuple.__reversed__() 
reversed_iterator = reversed(my_tuple)
for item in reversed_iterator:
    print(item)