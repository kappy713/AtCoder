n,k,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(k+1):
    if (sum(a)+i)//n>=m:
        exit(print(i))
print(-1)