h = int(input())

x = h
ans = 0
i = 1
while x > 0:
    ans += i
    x //= 2
    i *= 2
print(ans)