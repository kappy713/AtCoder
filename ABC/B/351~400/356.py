n,m = map(int, input().split())
a = list(map(int, input().split()))
X = [0 for _ in range(m)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        X[j] += x[j]

for i in range(m):
    if a[i] > X[i]:
        exit(print("No"))
print("Yes")