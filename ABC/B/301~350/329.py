n=int(input())
a=list(map(int,input().split()))

A=set(a)
A.remove(max(A))
print(max(A))