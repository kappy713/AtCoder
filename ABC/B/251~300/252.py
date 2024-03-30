n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_max=max(a)
max_index=[]
for i in range(n):
    if a[i]==a_max:
        max_index.append(i+1)
ans="No"
for i in b:
    if i in max_index:
        ans="Yes"
print(ans)