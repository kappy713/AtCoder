day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
s=input()
for i in range(7):
    if s==day[i]:
        exit(print(7-i))