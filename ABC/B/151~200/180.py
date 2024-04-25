n = int(input())
x = list(map(int, input().split()))

m = 0
for k in x:
    m += abs(k)
print(m)

e = 0
for k in x:
    e += abs(k) ** 2
print(e ** (1/2))

for i in range(n):
    x[i] = abs(x[i])
print(max(x))