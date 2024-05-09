n,d=map(int,input().split())
s =[input() for _ in range(n)]

ans,count = 0,0
for j in range(d):
    flag = True
    for i in range(n):
        if s[i][j] == "x":
            flag = False
            count = 0
            break
    if flag:
        count += 1
    ans = max(ans, count)
print(ans)