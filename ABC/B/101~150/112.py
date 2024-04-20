N, T = map(int, input().split())

ans = 10 ** 9
for _ in range(N):
    c, t = map(int, input().split())
    if t > T:
        pass
    else:
        ans = min(ans, c)
if ans == 10 ** 9:
    ans = "TLE"
print(ans)