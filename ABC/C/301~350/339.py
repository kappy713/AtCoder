n=int(input())
a=list(map(int,input().split()))

ans=[0]*n
ans[0]=a[0]
for i in range(1,n):
    ans[i]+=ans[i-1]+a[i]
start=abs(min(ans))
if min(ans)>=0:
    start=0
fin_ans=start
for i in range(n):
    fin_ans+=a[i]
print(fin_ans)