n=int(input())
s=input()

if n%2!=0:
    exit(print("No"))
num=len(s)//2
t1,t2=s[num:],s[:num]
print("Yes" if t1==t2 else "No")