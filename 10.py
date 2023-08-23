list1 = [10, 20, 25, 30, 35]  # odd
list2 = [40, 45, 60, 75, 90]  # even
list1[3]
oddlist = []
evenlist = []
# print(oddlist)
# oddlist.append("fds")
# print(oddlist)


for x in range(len(list1)):
    # print(x)

    if (list1[x] % 2 != 0):
        print(list1[x])
        oddlist.append(list1[x])
print(oddlist)


for x in range(len(list2)):
    # print(x)

    if list2[x] % 2 == 0:
        print(list2[x])
        evenlist.append(list2[x])
print(evenlist)

list3 = oddlist+evenlist
print(f"Third list is {list3}")
