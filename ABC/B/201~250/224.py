h,w=map(int,input().split())
A=[]
for _ in range(h):
    a=list(map(int,input().split()))
    A.append(a)

for i in range(h):
    for j in range(w):
        for x in range(i+1,h):
            for y in range(j+1,w):
                if A[i][j]+A[x][y]>A[x][j]+A[i][y]:
                    print("No")
                    exit()
print("Yes")