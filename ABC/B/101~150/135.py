n = int(input())
p = list(map(int, input().split()))

check = [i for i in range(1,n+1)]
if p == check:
    exit(print("YES"))

for i in range(n):
    for j in range(i,n):
        tmp = p.copy()
        tmp[i], tmp[j] = tmp[j], tmp[i]
        if tmp == check:
            exit(print("YES"))

print("NO")