# pallindrom

num = input("Enter : ")
reversenum = num[::-1]
print(f"entry is {num}")
print(f"reverse of entery is {reversenum}")

if num == reversenum:
    print("The given input is a pallindrome")
else:
    print("The given input is a not pallindrome")


# num = 3475
# print(num)
# strnum = str(num)
# strnum = list(strnum)
# # print(strnum[1])
# rvs_strnum = strnum
# # print(f"length of str is : {len(strnum)}")
# # print(f"length of reverse str is : {len(rvs_strnum)}")

# j = 0
# for x in range(len(strnum), 0, -1):
#     print(strnum[x-1], x-1)
#     strnum[x-1] = rvs_strnum[j]
#     print(j)
#     j = j + 1

# print("rvs str : ", rvs_strnum)
