s=input()
flag=False
ans=1
if s==s[::-1]:
    print(len(s))
    exit()
for i in range(len(s)):
    for j in range(len(s)):
        a=s[i:i+j]
        if s[i:i+j]==a[::-1]:
            flag=True
            if len(a)>ans:
                ans=len(a)
if flag:
    print(ans)
else:
    print(1)