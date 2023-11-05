a=[list(map(int,input().split())) for _ in range(3)]
n=int(input())

for _ in range(n):
    b=int(input())
    for i in range(3):
        for j in range(3):
            if b==a[i][j]:
                a[i][j]=0

for i in range(3):
    if a[i][0]==0 and a[i][1]==0 and a[i][2]==0:
        exit(print("Yes"))
    if (a[0][0]==0 and a[1][1]==0 and a[2][2]==0) or (a[0][2]==0 and a[1][1]==0 and a[2][0]==0) or (a[0][0]==0 and a[1][0]==0 and a[2][0]==0) or (a[0][1]==0 and a[1][1]==0 and a[2][1]==0) or (a[0][2]==0 and a[1][2]==0 and a[2][2]==0):
        exit(print("Yes"))
print("No")