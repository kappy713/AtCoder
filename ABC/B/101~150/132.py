n=int(input())
p=list(map(int,input().split()))

ans=0
for i in range(1,n-1):
    min_p=min(p[i-1],p[i],p[i+1])
    max_p=max(p[i-1],p[i],p[i+1])
    if min_p!=p[i] and max_p!=p[i]:
        ans+=1
print(ans)