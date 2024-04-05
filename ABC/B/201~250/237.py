h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

ans=[]
for j in range(w):
    tmp=[]
    for i in range(h):
        tmp.append(a[i][j])
    ans.append(tmp)
for x in ans:
    print(*x)