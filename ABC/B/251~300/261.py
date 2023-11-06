n=int(input())
a=[list(input()) for _ in range(n)]

for i in range(n):
    flag=True
    for j in range(i+1,n):
        if a[i][j]=="W" and a[j][i]!="L":
            flag=False
        if a[i][j]=="L" and a[j][i]!="W":
            flag=False
        if a[i][j]=="D" and a[j][i]!="D":
            flag=False
    if not flag:
        exit(print("incorrect"))
print("correct")