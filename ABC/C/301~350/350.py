n = int(input())
a = [0] + list(map(int, input().split()))
pos = [0] * (n+1)
for i in range(1, n+1):
    pos[a[i]] = i

ans = []
for i in range(1, n+1):
    if a[i] != i:
        j = pos[i]
        ans.append((min(i, j), max(i, j)))
        a[i], a[j] = a[j], a[i]
        pos[a[j]] = j
        pos[a[i]] = i

print(len(ans))
for x in ans:
    print(*x)