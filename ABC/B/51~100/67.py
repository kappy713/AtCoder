n,k=map(int,input().split())
l=list(map(int,input().split()))

l.sort()
longsum=0
for i in range(k):
    longsum+=l[-1-i]
print(longsum)