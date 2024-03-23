n=int(input())
a=list(map(int,input().split()))

a.sort()
flag=True
for i in range(n):
    if a[i]!=i+1:
        flag=False
print("Yes" if flag else "No")