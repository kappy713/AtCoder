n=int(input())
a=list(map(int, input().split()))

x=0
b=[0]*(n+1)
for i in range(n):
    if a[i]==-1:
        x=i+1
    else:
        b[a[i]]=i+1
    #print(b,a[i])
ans=[x]
#print(ans,b)
for _ in range(n-1):
    x=b[x]
    ans.append(x)
    #print(ans)
print(*ans)