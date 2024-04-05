n=input()

ans=0
for i in n:
    ans+=int(i)
print("Yes" if ans%9==0 else "No")