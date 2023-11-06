a,b,c,k=map(int,input().split())

if a>=k:
    print(1*k)
else:
    ans=1*a
    k-=a
    if b>=k:
        print(ans)
    else:
        k-=b
        ans+=-1*k
        print(ans)