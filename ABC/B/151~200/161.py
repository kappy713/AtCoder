n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = sum(a)
check = a_sum * (1 / (4 * m))
ans = 0
for x in a:
    if x>=check:
        ans += 1
print("Yes" if ans >= m else "No")