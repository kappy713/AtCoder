n = int(input())

ans = 0
for _ in range(n):
    l, r = map(int, input().split())
    seat = r - l + 1
    ans += seat
print(ans)