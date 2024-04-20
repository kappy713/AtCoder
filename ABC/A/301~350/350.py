s = input().strip()

if s == "ABC316":
    print("No")
elif 1 <= int(s[3:]) <= 349:
    print("Yes")
else:
    print("No")