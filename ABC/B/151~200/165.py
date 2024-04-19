x = int(input())

start = 100
ans = 0
while x > start:
    start += start // 100
    ans += 1
print(ans)