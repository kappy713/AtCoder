n=int(input())
s=input()

abc=[chr(i) for i in range(ord("A"), ord("Z")+1)]
for i in range(len(s)):
    if ord(s[i])+n>90:
        print(chr(ord(s[i])+n-26),end="")
    else:
        print(chr(ord(s[i])+n),end="")