s=input()

for i in range(len(s)):
    flag=False
    if (i+1)%2!=0:
        if s[i]=="R" or s[i]=="U" or s[i]=="D":
            flag=True
    else:
        if s[i]=="L" or s[i]=="U" or s[i]=="D":
            flag=True
    if not flag:exit(print("No"))
print("Yes")