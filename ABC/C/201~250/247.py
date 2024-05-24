n = int(input())

res = ["1"]
for i in range(2, n+1):
    res.append(res[-1] + " " + str(i) + " " + res[-1])

print(res[-1])