n=int(input())
a=list(map(int,input().split()))

ans=0
for x in a:
    ans+=(1/x)
print(1/ans)