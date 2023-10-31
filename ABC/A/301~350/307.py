n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
for i in range(1,n+1):
    ans[i-1]+=sum(a[7*(i-1):7*i])
print(*ans)