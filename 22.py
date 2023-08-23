# Checks if one set is a subset or superset of another
# set. If found, delete all elements from that set

set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}


print("First set is a subset of Second set :", set1.issubset(set2))
print("Second set is a subset of First set :", set2.issubset(set1))
print("First set is a supersubset of Second set :", set1.issuperset(set2))
print("Second set is a supersubset of First set :", set2.issuperset(set1))


if set1.issubset(set2) or set1.issuperset(set2):
    set1.clear()
elif set2.issubset(set1) or set2.issuperset(set1):
    set2.clear()
else:
    print("Neither is a subset of each other")


print("set1:", set1, "\n set2: ", set2)
# if set1 in set2:
#     print("set1 is a subset of set set2")
#     del set1
# elif set2 in set1:
#     print("set2 is a subset of set set1")
#     del set2
# else:
#     print("Neither are a subset of each other")
