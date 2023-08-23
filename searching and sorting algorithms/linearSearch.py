# Searching technique is done in sequential manner.
# O(n)
list = [2, 4, 67, 23, 85, 24, 6, 32, 78]

for i in range(len(list)):
    if list[i] == 78:
        print("element found", list[i], 'at index position', i)
        break
    i += i
