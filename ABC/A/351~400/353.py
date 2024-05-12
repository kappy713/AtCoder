n = int(input())
h = list(map(int, input().split()))

left = h[0]
index = -1
for i in range(1,n):
    if left < h[i]:
        index = i+1
        break
print(index)