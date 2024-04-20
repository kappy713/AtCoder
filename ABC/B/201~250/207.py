a, b, c, d = map(int, input().split())

ans = -1
blue, red = a, 0
for i in range(1, a+1):
    blue += b
    red += c
    if red * d >= blue:
        ans = i
        break
print(ans)