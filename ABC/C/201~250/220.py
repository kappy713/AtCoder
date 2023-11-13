n=int(input())
a=list(map(int,input().split()))
x=int(input())

s=x%sum(a)
ans=(x//sum(a))*n
for i in range(n):
    ans+=1
    if s-a[i]>=0:
        s-=a[i]
    else:
        exit(print(ans))