n,p=map(int,input().split())
a=list(map(int,input().split()))

ans=0
for x in a:
    if x<p:
        ans+=1
print(ans)