n,k,x = map(int, input().split())
a = list(map(int, input().split()))

print(*a[:k], x, *a[k:])