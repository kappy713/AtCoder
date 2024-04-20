n, m, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

fin = 0
ans = n
for i in range(m):
    ans -= ab[i][0] - fin
    if ans <= 0:
        break

    diff = ab[i][1] - ab[i][0]
    if diff > n - ans:
        ans = n
    else:
        ans += diff
    if ans <= 0:
        break

    fin = ab[i][1]
ans -= t - ab[i][1]
print("Yes" if ans > 0 else "No")