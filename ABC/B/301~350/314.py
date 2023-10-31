n=int(input())
a=[]
for _ in range(n):
    c=int(input())
    a.append(list(map(int,input().split())))
x=int(input())

min=38
ans=[]
for i in range(n):
    if x in a[i]:
        if len(a[i])<min:
            ans=[i+1]
            min=len(a[i])
        elif len(a[i])==min:
            ans.append(i+1)

print(len(ans))
print(*ans)