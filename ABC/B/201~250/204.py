n=int(input())
a=list(map(int,input().split()))

ans=0
for x in a:
    if x>10:
        ans+=(x-10)
print(ans)