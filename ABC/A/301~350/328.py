n,x=map(int,input().split())
s=list(map(int,input().split()))

ans=0
for i in range(n):
    if s[i]<=x:
        ans+=s[i]
print(ans)