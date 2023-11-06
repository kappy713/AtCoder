n=int(input())

ans=1
maxnum=0
for x in range(1,n+1):
    cnt=0
    X=x
    while x%2==0:
        x=x//2
        cnt+=1
    if maxnum<cnt:
        ans=X
        maxnum=cnt
print(ans)