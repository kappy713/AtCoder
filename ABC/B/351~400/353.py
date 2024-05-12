n,k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
tmp = k

for x in a:
    if tmp < x:
        ans += 1
        tmp = k
    tmp -= x
print(ans+1)