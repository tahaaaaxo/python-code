prev_num = 0

for x in range(10):
    current_num = prev_num+1
    print(
        f"current num :{current_num} , previous number:{prev_num} , sum :{prev_num+current_num}")
    prev_num = current_num
