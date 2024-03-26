n=int(input())
a=list(map(int,input().split()))

A=sorted(a)
for i in range(n):
    if A[-2]==a[i]:
        exit(print(i+1))