def swap_case(txt):
    # print("The given text is : ", txt)
    Alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
    Alphabets_upper = Alphabets_lower.upper()
    # print(Alphabets_lower, Alphabets_upper)
    txt_list = []
    for letters in txt:
        # print(letters)
        if letters in Alphabets_lower:
            txt_list.append(letters.upper())
            # print("alpha bet lower", letters.upper())
        elif letters in Alphabets_upper:
            txt_list.append(letters.lower())
            # print("alpha in upper", letters.lower())
        else:
            txt_list.append(letters)
            # print("aplha in num or sym")

    stringtxt = str("")
    for i in txt_list:
        # print(i, end="")
        stringtxt += i

    # print(stringtxt)

    return stringtxt


if __name__ == '__main__':
    txt = input()
    result = swap_case(txt)
    print(result)
