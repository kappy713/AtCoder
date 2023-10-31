n,m=map(int,input().split())
A=[]
for i in range(m):
    a=list(map(int,input().split()))
    A.append(a)
#print(A)

ans=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        flag=False
        for k in range(m):
            for l in range(n-1):
                if (A[k][l]==i and A[k][l+1]==j):
                    flag=True
                if (A[k][l]==j and A[k][l+1]==i):
                    flag=True
        if flag:
            pass
        else:
            ans+=1
print(ans)