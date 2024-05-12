n = int(input())
a = list(map(int, input().split()))

a.sort()

mod = 10**8
r = n
cnt,ans = 0,0
for i in range(n):
    r = max(r, i + 1)
    while r - 1 > i and a[r-1] + a[i] >= mod:
        r -= 1 
    cnt += n -r

for i in range(n):
    ans += a[i] * (n-1)
ans -= cnt * mod
print(ans)