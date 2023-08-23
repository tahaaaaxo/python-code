list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

listdict = dict()
for item in list:
    if item in listdict:
        listdict[item] += 1
    else:
        listdict[item] = 1

print(listdict)
