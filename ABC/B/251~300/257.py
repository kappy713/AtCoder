n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

check = [0] * n
for x in a:
    check[x-1] = 1

for x in l:
    if a[x-1] >= n:
        pass
    else:   
        if check[a[x-1]] == 1:
            pass
        else:
            check[a[x-1]] = 1
            check[a[x-1] - 1] = 0
            a[x-1] += 1
print(*a)