if __name__ == '__main__':
    n = int(input())
    mylist = []

    for i in range(n):
        # print(i)
        action_list = []
        action = (input())
        action_input_list = action.split()

        # print(action_input_list[2], action_list)
        if action_input_list[0] == "insert":
            mylist.insert(int(action_input_list[1]), int(action_input_list[2]))
            # print(mylist)
        elif action_input_list[0] == "print":
            print(mylist)
        elif action_input_list[0] == "remove":
            if int(action_input_list[1]) in mylist:
                mylist.remove(int(action_input_list[1]))
                # print("yes it is in list")
            else:
                pass
        elif action_input_list[0] == "append":
            mylist.append(int(action_input_list[1]))
        elif action_input_list[0] == "sort":
            mylist.sort()
        elif action_input_list[0] == "pop":
            mylist.pop()
        elif action_input_list[0] == "reverse":
            mylist.reverse()

# elif action_input_list[0] == "remove":
#             mylist.remove(action_input_list[1])
#         elif action_input_list[0] == "sort":
#             mylist.sort()
#         elif action_input_list[0] == "pop":
#             mylist.pop()
#         elif action_input_list[0] == "reverse":
#             mylist.reverse()
