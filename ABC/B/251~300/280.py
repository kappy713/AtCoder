n=int(input())
s=list(map(int,input().split()))

ans=[0]*n
ans[0]=s[0]
for i in range(1,n):
    ans[i]=s[i]-s[i-1]
print(*ans)