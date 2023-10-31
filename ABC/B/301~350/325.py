n=int(input())
cnt=[0]*24
for i in range(n):
    w,x=map(int,input().split())
    cnt[x]+=w

ans=0
for i in range(24):
    sum=0
    for j in range(9):
        sum+=cnt[(i+j)%24]
    ans=max(ans,sum)

print(ans)