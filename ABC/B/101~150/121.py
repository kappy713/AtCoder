n,m,c=map(int,input().split())
b=list(map(int,input().split()))
A=[]
for _ in range(n):
    a=list(map(int,input().split()))
    A.append(a)

cnt=0
for i in range(n):
    sum=c
    for j in range(m):
        sum+=A[i][j]*b[j]
    if sum>0:
        cnt+=1
print(cnt)