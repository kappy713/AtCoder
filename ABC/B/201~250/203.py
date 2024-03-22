n,k=map(int,input().split())

ans=0
for i in range(1,n+1):
    I=str(i)
    for j in range(1,k+1):
        J=str(j)
        tmp=I+"0"+J
        ans+=int(tmp)
print(ans)