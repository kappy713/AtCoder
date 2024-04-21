n = int(input())
a = list(map(int, input().split()))

gcd = (0, 0)
for i in range(2, 1001):
    cnt = 0
    for x in a:
        if x % i == 0:
            cnt +=1
        if gcd[1] < cnt:
            gcd = (i, cnt)
print(gcd[0])