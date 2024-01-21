s=input()

flag=True
a,b,c=[],[],[]
for i in range(len(s)):
    if s[i]=="A":
        a.append(i)
    elif s[i]=="B":
        b.append(i)
    else:
        c.append(i)

x=0

if not a:
    pass
else:
    for i in range(len(a)):
        if a[i]==x:
            x+=1
        else:
            flag=False
if not b:
    pass
else:
    for i in range(len(b)):
        if b[i]==x:
            x+=1
        else:
            flag=False
if not c:
    pass
else:
    for i in range(len(c)):
        if c[i]==x:
            x+=1
        else:
            flag=False
print("Yes" if flag else "No")