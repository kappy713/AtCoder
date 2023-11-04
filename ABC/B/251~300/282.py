n,m=map(int,input().split())
S=[]
for _ in range(n):
    s=input()
    S.append(s)

ans=0
for i in range(n):
    for j in range(i+1,n):
        flag=True
        for k in range(m):
            if S[i][k]=="x" and S[j][k]=="x":
                flag=False
        if flag:
            ans+=1
print(ans)