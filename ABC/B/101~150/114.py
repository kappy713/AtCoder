s=input()

ans=10**9
for i in range(len(s)-2):
    x=s[i]+s[i+1]+s[i+2]
    X=int(x)
    check=abs(X-753)
    ans=min(ans,check)
print(ans)