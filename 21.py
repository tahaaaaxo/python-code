# Find the intersection (common) of two
# sets and remove those elements from the first set
list1 = {23, 42, 65, 57, 78, 83, 29}
list2 = {57, 83, 29, 67, 73, 43, 48}

intersection = list1.intersection(list2)
# list1.remove(list1.intersection(list2))
print(list1)
print(list2)
for item in intersection:
    list1.remove(item)

print(list1)


# if x in list2:

# print("Removing :", x)

# print(list1)
