n,m=map(int,input().split())

N,M=[],[]
for i in range(n):
    N.append(2*(i+1))
for j in range(m):
    M.append(2*j+1)
ans=0

for i in range(n):
    for j in range(m):
        if (N[i]+M[j])%2==0:
            ans+=1
for i in range(n):
    for j in range(i+1,n):
        if (N[i]+N[j])%2==0:
            ans+=1
for i in range(m):
    for j in range(i+1,m):
        if (M[i]+M[j])%2==0:
            ans+=1
print(ans)