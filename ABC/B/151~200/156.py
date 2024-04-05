n,k=map(int,input().split())

ans=[]
while n>=k:
    ans.append(str(n%k))
    n//=k
ans.append(str(n))
print(len(ans))