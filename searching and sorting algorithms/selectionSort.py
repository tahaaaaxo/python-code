# In this sorting technique the list is dirided into 2 parts
# (1)sorted (2)unsorted
# O(n^2)

import random_list
list = random_list.random_l()

list = [8, 11, 27, 3, 1, 6, 4]
print(list)

for i in range(len(list)):
    print(list[i], "----min----")
    for j in range(i+1, len(list)):
        print(list[j])
        if list[i] > list[j]:
            i = j

    list[i], list[j] = list[j], list[i]
    print(f"swapped {list[i]} and {list[j]}")
    print(list)

print(list)
