n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: abs(x[0] - x[1]))

ans = 0
for i in range(n-1):
    ans += ab[i][0]
ans += ab[-1][1]
print(ans)