s=input()

ans=[]
for i in reversed(range(len(s))):
    if s[i]!=".":
        ans.append(s[i])
    else:
        break
for i in reversed(range(len(ans))):
    print(ans[i],end="")