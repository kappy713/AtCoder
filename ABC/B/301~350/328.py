n=int(input())
d=list(map(int,input().split()))

ans=0
for i in range(1,n+1):
    for j in range(1,d[i-1]+1):
        I=str(i)
        J=str(j)
        if set(I)==set(J) and len(set(I))==1:
            ans+=1
print(ans)