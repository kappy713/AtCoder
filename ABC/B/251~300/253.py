h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]

o=[]
for i in range(h):
    for j in range(w):
        if s[i][j]=="o":
            o.append(i+1)
            o.append(j+1)
ans=abs(o[2]-o[0])+abs(o[3]-o[1])
print(ans)