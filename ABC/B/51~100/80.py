n = input()

check = 0
for x in n:
    check += int(x)
print("Yes" if int(n) % check == 0 else "No")