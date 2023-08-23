# find second lowest and print their name in order
students = []
list_of_sec_low = []
list_of_name = []

n = int(input())

for studs in range(n):  # takes input and appends it to students[]
    name = input()
    score = float(input())
    students.append([score, name])

students.sort()  # sorts students[]

# print(f"sorted student list is : {students}")

for i in range(len(students)):  # finds second lowest and saves it in sec_low_stud
    if students[i][0] < students[i+1][0]:
        sec_low_stud = students[i+1]
        break

# print(f"second lowest is : {sec_low_stud}")

for w in range(len(students)):  # appends all second lowests to list_of_sec_low[]
    if students[w][0] == sec_low_stud[0]:
        list_of_sec_low.append(students[w])

for items in list_of_sec_low:  # appends only the name of sec low to list_of_name[]
    list_of_name.append(items[1])

list_of_name.sort()  # sorts list_of_names[]

for names in list_of_name:
    print(names)
