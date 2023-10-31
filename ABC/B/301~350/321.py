n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(-1)

for i in range(0,101):
    A=a.copy()
    A[n-1]=i
    A.sort()
    sum=0
    for j in range(1,n-1):
        sum+=A[j]
    if sum>=x:
        print(i)
        exit()
print(-1)