n=int(input())
flag=False
for x in range(50):
    for y in range(50):
        if n==(2**x)*(3**y):
            flag=True

for y in range(50):
    for x in range(50):
        if n==(2**x)*(3**y):
            flag=True

if flag:
    print("Yes")
else:
    print("No")