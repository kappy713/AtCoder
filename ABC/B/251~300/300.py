h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
b=[list(input()) for _ in range(h)]

#sの上限はh-1回,tの上限はw-1回
for s in range(h):
    for t in range(w):
        flag=True
        for i in range(h):
            for j in range(w):
                if a[(i-s+h)%h][(j-t+w)%w]!=b[i][j]:
                    flag=False
        if flag:
            exit(print("Yes"))
print("No")