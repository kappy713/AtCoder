n = int(input())
d, x = map(int, input().split())

ans = x
for _ in range(n):
    a = int(input())
    check = (d - 1) // a + 1
    ans += check
print(ans)