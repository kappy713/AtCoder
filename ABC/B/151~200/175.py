n=int(input())
l=list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum=l[i]+l[j]+l[k]
            maxl=max(l[i],l[j],l[k])
            if (l[i]!=l[j] and l[j]!=l[k] and l[k]!=l[i]) and (maxl<sum-maxl):
                ans+=1
print(ans)