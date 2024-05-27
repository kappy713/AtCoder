n = int(input())
h = list(map(int, input().split()))

start = h[0]
ans, cnt = 0, 0
for i in range(1, n):
    now, next = h[i-1], h[i] 
    if now < next:
        ans = max(cnt, ans)
        cnt = 0
    else:
        cnt += 1
ans = max(cnt, ans)
print(ans)