n=int(input())
h=list(map(int,input().split()))

high=h[0]
for i in range(1,n):
    if high<h[i]:
        high=h[i]
    else:
        break
print(high)