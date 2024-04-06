import math
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]

ans=[]
for i in range(n):
    dis=0
    for j in range(n):
        if i==j:
            pass
        else:
            tmp=math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)
            if dis<tmp:
                dis=tmp
                maxnum=j+1
    ans.append(maxnum)
for i in ans:
    print(i)