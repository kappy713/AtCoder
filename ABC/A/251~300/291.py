s=list(input())
for i in range(len(s)):
    flag=s[i].isupper()
    if flag:
        print(i+1)
    else:
        continue