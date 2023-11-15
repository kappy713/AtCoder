n=int(input())
ans=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    ans[i]+=a+b
for i in range(n):
    print(ans[i])