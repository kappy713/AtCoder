n,m=map(int,input().split())
c=list(input().split())
d=list(input().split())
p=list(map(int,input().split()))

ans=0
for s in c:
    price=p[0]
    for i in range(m):
        if s==d[i]:
            price=p[i+1]
            break
    ans+=price
print(ans)