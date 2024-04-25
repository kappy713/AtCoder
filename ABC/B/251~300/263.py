n = int(input())
p = list(map(int, input().split()))

ans = 0
while n != 1:
    n = p[n-2]
    ans += 1
print(ans)