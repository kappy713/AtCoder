n,d=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(n):
    for j in range(i+1,n):
        check=0
        for k in range(d):
            check+=abs(x[i][k]-x[j][k])**2
        check=check**0.5
        if check.is_integer():
            ans+=1
print(ans)