# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(list):

    # Traverse through 1 to len(list)
    for i in range(1, len(list)):

        key = list[i]
        # Move elements of list[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


# Driver code to test above
list = [12, 11, 13, 5, 6]
print(list)
# insertionSort(list)
for i in range(1, len(list)):
    print(i)

    key = list[i]
    # Move elements of list[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and key < list[j]:
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = key

print(list)
