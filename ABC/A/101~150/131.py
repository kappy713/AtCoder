s=input()
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        exit(print("Bad"))
print("Good")