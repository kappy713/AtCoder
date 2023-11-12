n,t=map(int,input().split())
a=list(map(int,input().split()))

s=t%sum(a)
for i in range(n):
    if s<a[i]:
        exit(print(i+1,s))
    else:
        s-=a[i]