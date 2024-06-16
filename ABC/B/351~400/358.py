n,a = map(int, input().split())
t = list(map(int, input().split()))

ans = [0 for _ in range(n)]
ans[0] = t[0] + a
for i in range(1, n):
    if ans[i-1] > t[i]:
        ans[i] = ans[i-1] + a
    else:
        ans[i] = t[i] + a

for x in ans:
    print(x)