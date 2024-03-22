n,x=map(int,input().split())
a=list(map(int,input().split()))

price=0
for i in range(n):
    if (i+1)%2==0:
        a[i]-=1
    price+=a[i]
print("Yes" if price<=x else "No")