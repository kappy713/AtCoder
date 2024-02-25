s=input()
for i in range(len(s)):
    if s.count(s[i])==1:
        exit(print(i+1))