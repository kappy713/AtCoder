n,x=map(int,input().split())
s=input()

ans=x
for i in s:
    if i=="x" and ans>0:
        ans-=1
    elif i=="o":
        ans+=1
print(ans)