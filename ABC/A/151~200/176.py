n,x,t=map(int,input().split())

ans,X=0,0
while X<n:
    X+=x
    ans+=t
print(ans)