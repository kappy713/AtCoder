n,s,m,l=map(int,input().split())

ans=10**9
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if 6*i+8*j+12*k>=n:
                ans=min(ans,i*s+j*m+k*l)
print(ans)