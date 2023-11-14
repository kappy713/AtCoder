x,n=map(int,input().split())
p=list(map(int,input().split()))

if n==0:
    exit(print(100))
x_list=[1]*100
for i in range(n):
    x_list[p[i]-1]=0
minnum=10**9
for i in range(100):
    if x_list[i]!=0:
        check=abs(x-(i+1))
    if minnum>check:
        ans=i+1
        minnum=min(minnum,check)
print(x_list,ans)