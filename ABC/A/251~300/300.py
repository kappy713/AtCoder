n,a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(n):
    if a+b==c[i]:
        ans=i+1
        break
print(ans)