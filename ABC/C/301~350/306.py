n=int(input())
a=list(map(int,input().split()))

tmp=[0 for _ in range(3*n)]
ans=[]
for i in a:
    tmp[i]+=1
    if tmp[i]==2:
        ans.append(i)
print(*ans)