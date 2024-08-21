
my_set = {1, 2, 3, 4, 5}

# 1. add()
print("Original set: ", my_set)
my_set.add(6)
print("Set after add(): ", my_set)

# 2. remove() 
print("Original set: ", my_set)
my_set.remove(4)
print("Set after remove(): ", my_set)

# 3. clear() 
print("Original set: ", my_set)
my_set.clear()
print("Set after clear(): ", my_set)

# new set
my_set = {1, 2, 3, 4, 5}

# 4. copy() 
my_set_copy = my_set.copy()
print("Original set: ", my_set)
print("Copied set: ", my_set_copy)

# 5. pop() 
print("Original set: ", my_set)
popped_element = my_set.pop()
print("Popped element: ", popped_element)
print("Set after pop(): ", my_set)

# 6. update() 
print("Original set: ", my_set)
my_set.update({6, 7, 8})
print("Set after update(): ", my_set)

# 7. union() 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set1: ", set1)
print("Set2: ", set2)
union_set = set1.union(set2)
print("Union set: ", union_set)

# 8. difference() 
print("Set1: ", set1)
print("Set2: ", set2)
difference_set = set1.difference(set2)
print("Difference set: ", difference_set)

# 9. difference_update()
print("Original set1: ", set1)
set1.difference_update(set2)
print("Set1 after difference_update(): ", set1)

# 10. discard() 
print("Original set: ", my_set)
my_set.discard(6)
print("Set after discard(): ", my_set)

# 11. intersection() 
print("Set1: ", set1)
print("Set2: ", set2)
intersection_set = set1.intersection(set2)
print("Intersection set: ", intersection_set)

# 12. intersection_update() 
print("Original set1: ", set1)
set1.intersection_update(set2)
print("Set1 after intersection_update(): ", set1)

# 13. isdisjoint() 
print("Set1: ", set1)
print("Set2: ", set2)
print("Is disjoint: ", set1.isdisjoint(set2))

# 14. issubset() 
print("Set1: ", set1)
print("Set2: ", set2)
print("Is subset: ", set1.issubset(set2))

# 15. issuperset() 
print("Set1: ", set1)
print("Set2: ", set2)
print("Is superset: ", set1.issuperset(set2))

# 16. symmetric_difference() 
print("Set1: ", set1)
print("Set2: ", set2)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference set: ", symmetric_difference_set)

# 17. symmetric_difference_update() 
print("Original set1: ", set1)
set1.symmetric_difference_update(set2)
print("Set1 after symmetric_difference_update(): ", set1)