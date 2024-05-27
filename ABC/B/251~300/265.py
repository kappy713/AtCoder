n,m,t = map(int, input().split())
a = list(map(int, input().split()))

xy = []
for i in range(m):
    XY = list(map(int, input().split()))
    xy.append(XY)

for i in range(n-1):
    t -= a[i]
    m += 1
    if t <= 0:
        exit(print("No"))
    if xy and xy[0][0] == m:
        t += xy[0][1]
        xy.pop(0)
print("Yes")