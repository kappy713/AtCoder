n=int(input())
ans=0
for i in range(n):
    s=input()
    if s=="For":
        ans+=1
    else:
        ans-=1
if ans>0:
    print("Yes")
else:
    print("No")