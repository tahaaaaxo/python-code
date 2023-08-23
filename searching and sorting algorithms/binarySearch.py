# It is Fast searching algorithm with time complexity O(logn)
# Based on divide & conquer
# Data items should be in sorted manner.

list = [2, 5, 11, 16, 23, 35, 35, 37, 40, 46, 49, 52, 56, 57, 59]

low = 0
high = len(list)-1
num_to_find = 35
i = 1

while high >= low:
    mid = (high+low)//2
    print("try no. :", i)
    i += 1

    if num_to_find == list[mid]:
        print(num_to_find, "found at position", mid)
        break
    elif num_to_find > list[mid]:
        low = mid+1
    else:
        high = mid-1
