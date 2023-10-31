n=int(input())
ans=[[0]*100 for i in range(100)]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    for i in range(a,b):
        for j in range(c,d):
            ans[i][j]=1

count=0
for i in range(100):
    for j in range(100):
        if ans[i][j]==1:
            count+=1

print(count)