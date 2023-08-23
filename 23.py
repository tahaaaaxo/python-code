# Iterate a given list and check if a given element exists as a key’s value
# in a dictionary. If not, delete it from the list

roll_number = [95, 47, 64, 69, 37,  97, 76, 66]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
# roll_number[:] = [item for item in range(10)]
print(roll_number)

# for x in roll_number:
#     # print(x)
#     if x not in sample_dict.values():
#         print(x, "not in dict")
#         roll_number.remove(x)
#     else:
#         print(x, "is in dict")

# print(roll_number)
# print(sample_dict.values())

# if 47 in roll_number:
#     print("true")
#     roll_number.remove(47)
# else:
#     print("false")

# print(roll_number)
