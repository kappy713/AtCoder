h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

min_num=10**9
for i in range(h):
    for j in range(w):
        min_num=min(min_num,a[i][j])
cnt=0
for i in range(h):
    for j in range(w):
        cnt+=(a[i][j]-min_num)
print(cnt)