n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans="Yes"
for i in b:
    if i in a:
        a.remove(i)
    else:
        ans="No"
print(ans)