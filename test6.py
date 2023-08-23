# ininini  ini is not happening

def count_substring(string, sub_string):
    no_of_substring = 0
    print(string, sub_string)
    for i in range(len(string)):  # iterates through string
        for j in range(len(sub_string)):  # iterates through sub string
            print("now at", i, j)
            if string[i] == sub_string[j]:  # checks if the letters are the same
                newstring = ""
                print("matching at ", i, j)
                for ni in range(i, i+len(sub_string)):
                    if i+len(sub_string) < len(string):
                        print(string[ni])
                        newstring += string[ni]
                        print(newstring)
                        if newstring == sub_string:
                            no_of_substring += 1
                            print("now the no of substrings are : ",
                                  no_of_substring)
                    else:
                        # pass
                        print("string index out of range")

    return no_of_substring


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print("no. of substrings is :", count)
