# Remove duplicates from a list and create a tuple and find
# the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("original list :", sample_list)
list = []

for x in sample_list:
    if x not in list:
        list.append(x)


list = tuple(list)
print("tuple", list)

y = list[0]
# print(y)

for x in list:
    if x > y:
        y = x

print("Max :", y)

for x in list:
    if x < y:
        y = x

print("Min :", y)
