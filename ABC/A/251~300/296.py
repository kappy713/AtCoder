n=int(input())
s=input()
if n==1:
    print("Yes")
    exit()
flag=True
for i in range(n-1):
    if (s[i]=="M" and s[i+1]=="M") or (s[i]=="F" and s[i+1]=="F"):
        flag=False
if flag:print("Yes")
else:print("No") 