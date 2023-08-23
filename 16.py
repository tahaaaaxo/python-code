list1 = [0, 1, 2, 3, 4, 5]
list2 = [0, 1, 2, 3, 4, 5]
list3 = []

list3.extend(list1[1::2])
list3.extend(list2[::2])
print(list3)
