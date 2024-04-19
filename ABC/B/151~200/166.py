n, k = map(int, input().split())
check = [0] * n
for _ in range(k):
    d = int(input())
    a = list(map(int,input().split()))

    for x in a:
        check[x-1] = 1
print(check.count(0))