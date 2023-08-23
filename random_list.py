import random


def random_l():
    list = []
    num = int(input("Enter lenght of list :"))
    start = int(input("Enter starting range :"))
    end = int(input("Enter ending range :"))
    for i in range(num):
        list.append(random.randint(start, end))
    return list
