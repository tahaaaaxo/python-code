income = 100000
tax = 0
print(f"Income is {income}")
if income > 20000:
    income = income-10000  # first 10000
    tax = 10000*0.1  # second 10000
    income = income-10000
    tax = tax + income*0.2  # next amount
    print("income tax is : ", tax)
elif income > 10000:
    income = income-10000  # first 10000
    tax = income*0.1  # second 10000
    print("income tax is : ", tax)
else:
    print("income tax is : ", tax)
