
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     mytuple = tuple(integer_list)
#     print(type(mytuple), mytuple, hash(mytuple))

if __name__ == '__main__':
    n = int(input())  # Number of elements in the tuple
    integer_list = map(int, input().split())  # Space-separated integers

    # Create a tuple from the input integers
    integer_tuple = tuple(integer_list)

    # Calculate the hash value of the tuple and print it
    hash_value = hash(integer_tuple)
    print(hash_value)
