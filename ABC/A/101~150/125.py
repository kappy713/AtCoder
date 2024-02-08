a,b,t=map(int,input().split())
A=a
ans=0
while A<t+0.5:
    ans+=b
    A+=a
print(ans)