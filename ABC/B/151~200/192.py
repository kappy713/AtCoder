s=input()

flag=False
for i in range(len(s)):
    if s[i].islower() and (i+1)%2!=0:
        flag=True
    elif s[i].isupper() and (i+1)%2==0:
        flag=True
    else:
        flag=False
        break
print("Yes" if flag else "No")