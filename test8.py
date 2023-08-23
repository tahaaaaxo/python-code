import textwrap


def wrap(string, max_width):
    # print(string, max_width)
    str_list = list(string)
    # print(str_list)

    for i in range(1, len(str_list)+1):
        print(str_list[i-1], end="")
        if i % (max_width) == 0:
            print("")

    return ""


if __name__ == '__main__':
    # print(6 % 3)
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
