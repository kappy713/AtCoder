n, x = map(int, input().split())
a = list(map(int, input().split()))

check = [False] * n
ans = 0
while not check[x-1]:
    ans += 1
    check[x-1] = True
    x = a[x-1]
    print(x,check)
print(ans)