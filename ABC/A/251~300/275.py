n=int(input())
h=list(map(int,input().split()))

ans=1
maxnum=h[0]
for i in range(1,n):
    if h[i]>maxnum:
        ans=i+1
        maxnum=h[i]
print(ans)