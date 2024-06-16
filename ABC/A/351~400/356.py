n,l,r = list(map(int, input().split()))

a = [i for i in range(1, n+1)]
a_part = a[l-1:r]
a[l-1:r] = a_part[::-1]
print(*a)