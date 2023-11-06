n,k=map(int,input().split())
h=list(map(int,input().split()))

h.sort()
for i in range(min(n,k)):
    h[-1-i]=0
print(sum(h))