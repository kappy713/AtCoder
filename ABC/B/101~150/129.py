n=int(input())
w=list(map(int,input().split()))

minnum=10**9
for s in range(n-1):
    check=abs(sum(w[:s+1])-sum(w[s+1:]))
    minnum=min(minnum,check)
print(minnum)