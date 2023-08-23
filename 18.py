# Slice list into 3 equal chunks and reverse each chunk
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_len = int(len(list)/3)

start = 0
end = chunk_len

for x in range(3):
    index = slice(start, end)
    chuck = list[index]
    print(chuck)
    print(chuck[::-1])
    start = end
    end += chunk_len


# chunck1 = list[:chunk_len]
# # print(chunck1)
# chunck2 = list[chunk_len:len(list)-chunk_len]
# # print(chunck2)
# chunck3 = list[len(list)-chunk_len:]
# # print(chunck3)

# chunck1rvs = chunck1[::-1]
# chunck2rvs = chunck2[::-1]
# chunck3rvs = chunck3[::-1]

# print("Original list : ", list)
# print("  chunk 1 : ", chunck1)
# print("reverse chunk 1:", chunck1rvs)
# print("  chunk 2 : ", chunck2)
# print("reverse chunk 2:", chunck2rvs)
# print("  chunk 3 : ", chunck1)
# print("reverse chunk 3:", chunck3rvs)
