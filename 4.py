def remove_char(word, num):
    print(f"Word : {word}, deletion number : {num}")
    new_word = word[num:]

    print(f"new word :{new_word}")
    return new_word


remove_char("pynative", 4)
