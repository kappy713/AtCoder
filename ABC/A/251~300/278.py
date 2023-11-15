n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=a
if n<=k:
    ans=[0]*n
    print(*ans)
    exit()
for i in range(k):
    for j in range(n-i-1):
        ans[j]=a[j+1]
    ans[j+1]=0
print(*ans)