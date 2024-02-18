n=int(input())
ans=[]
for i in range(2*n+1):
    if i%2==0:
        ans.append(1)
    else:
        ans.append(0)
print(*ans,sep="")