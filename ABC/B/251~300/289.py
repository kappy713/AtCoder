n,m=map(int,input().split())
a=list(map(int,input().split()))

ans=[0]
for i in range(1,n+1):
    if i not in a:
        ans.append(i)
        j=i-1
        while j not in ans:
            ans.append(j)
            j-=1
print(*ans[1:])