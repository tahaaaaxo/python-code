# Write a program to remove the item present at index 4 and add
# it to the 2nd position and at the end of the list.

list1 = [34, 54, 67, 89, 11, 43,  94]
print("Original list :", list1)


temp = list1[4]

del list1[4]
list1.insert(2, temp)
print("List after removing 4th index :", list1)
list1.append(temp)

print("List after adding at last :", list1)
