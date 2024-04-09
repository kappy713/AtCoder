n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

ans=0
for i in range(n):
    if i>0:
        if a[i-1]+1==a[i]:
            ans+=b[a[i]-1]+c[a[i-1]-1]
        else:
            ans+=b[a[i]-1]
    else:
        ans+=b[a[i]-1]
print(ans)