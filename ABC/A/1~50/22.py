n,s,t=map(int,input().split())
w=int(input())

if s<=w<=t:
    ans=1
else:
    ans=0
for i in range(n-1):
    a=int(input())
    w+=a
    if s<=w<=t:
        ans+=1
print(ans)