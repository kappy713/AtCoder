n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 10**9
for i in range(n):
    for j in range(n):
        ans = min(ans, ab[i][0] + ab[j][1] if i == j else max(ab[i][0], ab[j][1]))
print(ans)