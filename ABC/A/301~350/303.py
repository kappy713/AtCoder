n=int(input())
s=input()
t=input()
Flag=True
for i in range(n):
    if s[i]=="0" and t[i]=="o"or(s[i]=="o" and t[i]=="0"):
        continue
    if (s[i]=="1" and t[i]=="l")or(s[i]=="l" and t[i]=="1"):
        continue
    if s[i]!=t[i]:
        Flag=False
if Flag:print("Yes")
else:print("No")