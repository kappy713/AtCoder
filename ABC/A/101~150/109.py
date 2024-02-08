a,b=map(int,input().split())
for c in range(1,4):
    if (a*b*c)%2!=0:
        exit(print("Yes"))
print("No")