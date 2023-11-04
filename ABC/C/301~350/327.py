a=[list(map(int,input().split())) for _ in range(9)]

#条件1の確認
for i in range(9):
    num=[0]*9
    for j in range(9):
        num[a[i][j]-1]=1
    if sum(num)!=9:
        print("No")
        exit()

#条件2の確認
for j in range(9):
    num=[0]*9
    for i in range(9):
        num[a[i][j]-1]=1
    if sum(num)!=9:
        print("No")
        exit()

#条件3の確認
for i in range(0,9,3):
    for j in range(0,9,3):
        num=[0]*9
        for x in range(i,i+3):
            for y in range(j,j+3):
                num[a[x][y]-1]=1
        if sum(num)!=9:
            print("No")
            exit()
print("Yes")