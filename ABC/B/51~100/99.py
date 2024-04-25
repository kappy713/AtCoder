a,b = map(int, input().split())

dis = b - a
ans = 0
for i in range(1, dis+1):
    ans += i
print(ans - b)