# In Bubble Sorting technique, each pair of adjacent is
# compared and elements are swapped if they are not in order
# Worst case time complexity = 0(n^2)

import random_list

# list = random_list.random_l()
list = [8, 11, 27, 3, 1, 6, 4]

print("Unsorted List :", list)

for i in range(len(list)-1, 0, -1):
    # prin  t("i is ", i)
    for j in range(i):
        # print("j is ", j)
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print("Sorted List : ", list)
