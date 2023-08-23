def print_welcome_logo(thickness, width):
    c = '.|.'

    # Top cone
    for i in range(thickness // 2):
        print((c * (i * 2 + 1)).center(width, '-'))

    # Welcome message
    print('WELCOME'.center(width, '-'))

    # Bottom cone
    for i in range(thickness // 2 - 1, -1, -1):
        print((c * (i * 2 + 1)).center(width, '-'))


if __name__ == '__main__':
    # print("nefiefex")
    thickness, width = map(int, input().split())
    print_welcome_logo(thickness, width)
