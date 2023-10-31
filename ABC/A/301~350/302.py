a,b=map(int,input().split())
ans=a//b
if a-ans*b>0:
    ans+=1
print(ans)