n,m,x = map(int, input().split())
a = list(map(int, input().split()))

cost1, cost2 = 0, 0
for i in a:
    if i <= x:
        cost1 += 1
    if i >= x:
        cost2 += 1
print(min(cost1, cost2))