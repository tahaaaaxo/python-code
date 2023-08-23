# correct combination : 1 2 2 2 1 2 2 2 3 1 2 2
jar_4_g = 0
jar_3_g = 0


def fill():
    # print("fill")
    global jar_4_g
    global jar_3_g

    jar_to_fill = input(
        "\n 4 gallon jar (1) \n 3 gallon jar (2) \n enter the jar you want to fill : ")

    if jar_to_fill == "1":
        jar_4_g = 4
        print("4 gallon jar filled ")
    elif jar_to_fill == "2":
        jar_3_g = 3
        print("3 gallon jar filled ")
    else:
        print("invalid input")


def pour():
    # print("pour")
    global jar_4_g
    global jar_3_g

    jar_to_pour = input(
        "\n 4 gallon jar into 3 gallon jar (1)\n 3 gallon jar into 4 gallon jar (2) \n enter your input: ")
    if jar_to_pour == "1":
        if (jar_4_g+jar_3_g) > 3:
            jar_4_g = jar_4_g-(3-jar_3_g)
            jar_3_g = 3
        else:
            jar_3_g += jar_4_g
            jar_4_g = 0
        print("4 gallon jar poured into 3 gallon jar ")
    elif jar_to_pour == "2":
        if (jar_3_g+jar_4_g) > 4:
            jar_3_g = jar_3_g-(4-jar_4_g)
            jar_4_g = 4
        else:
            jar_4_g += jar_3_g
            jar_3_g = 0
        print("3 gallon jar poured into 4 gallon jar ")
    else:
        print("invalid input")


def empty():
    # print("empty")
    global jar_4_g
    global jar_3_g
    jar_to_empty = input(
        "\n to empty 4 gallon jar (1) \n to empty 3 gallon jar (2) \n Enter your choise : ")
    if jar_to_empty == "1":
        jar_4_g = 0
    elif jar_to_empty == "2":
        jar_3_g = 0
    else:
        print("invalid input")

# def view():
#     print("view")
    #   global jar_4_g
    # global jar_3_g
#     print(f"4 gallon jar has {jar_4_g} and 3 gallon jar has {jar_3_g}")


print("---------Your have 10 attempts---------")
print("You have 2 jars , one 4 gallons and one 3 gallons , you have to get exatly 2 gallons of water in 4 gallon jar , Actions to perform are  , (1)fill,(2)pour,(3)empty,(4)view")
for i in range(10):

    print(f"\n --------- attempt number : {i+1} ---------")
    print(
        f"4 gallon jar has {jar_4_g} gallons and 3 gallon jar has {jar_3_g} gallons")
    choise = input(
        " to fill(1) \n to pour (2) \n to empty (3)\n Enter your choise : ")  # \n to view (4)

    if choise == "1":
        fill()
    elif choise == "2":
        pour()
    elif choise == "3":
        empty()
    # elif choise=="4":
    #     view()
    else:
        print("invalid input")

    if jar_4_g == 2:
        print("\n ---- You've succeded 👍🥳 ---- ")
        break

    if i == 9:
        print("---attempts over--- ")
        break
