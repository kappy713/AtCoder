n=int(input())
a=list(map(int,input().split()))

minA=min(a)
maxA=max(a)
ans=[0]*(maxA-minA+1)
for i in range(n):
    ans[a[i]-minA]=1
for i in range(n):
    if ans[i]==0:
        num=minA+i
        break
print(num)