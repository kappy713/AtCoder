n=int(input())
x=list(map(int,input().split()))

minnum=10**9
for i in range(101):
    check=0
    for j in range(n):
        check+=(x[j]-(i))**2
    minnum=min(minnum,check)
print(minnum)