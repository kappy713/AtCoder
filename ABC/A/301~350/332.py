n,s,k=map(int,input().split())
pq=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(n):
    p,q=pq[i]
    ans+=p*q
if ans<s:
    print(ans+k)
else:
    print(ans)