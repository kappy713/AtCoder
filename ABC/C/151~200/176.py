n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(1,n):
    print(a)
    if a[i-1]>=a[i]:
        pass
    else:
        while a[i-1]>=a[i]:
            a[i-1]+=1
            ans+=1
            print(a)
print(ans)