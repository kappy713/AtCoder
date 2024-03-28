n=int(input())
min_price=10**9
for i in range(n):
    a,p,x=map(int,input().split())
    res=x-a
    if res>0:
        min_price=min(min_price,p)
if min_price==10**9:
    print(-1)
else:
    print(min_price)