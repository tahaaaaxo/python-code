# base = int(input("Base : "))
# expo = int(input("Expo : "))
base = 3
expo = 2
ans = 1
for x in range(expo):
    ans = ans*base
# ans = base ^ expo
print(f" {base} ^ {expo} = {ans}")
