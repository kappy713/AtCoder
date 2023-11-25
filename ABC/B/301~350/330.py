n,l,r=map(int,input().split())
a=list(map(int,input().split()))

x=[0 for i in range(n)]
for i in range(n):
    if a[i]<=l:
        x[i]=l
    elif a[i]>=r:
        x[i]=r
    elif l<=a[i]<=r:
        x[i]=a[i]
print(*x)