n=int(input())
s=input()
a,b,c=0,0,0
if n==3:
    print(3)
    exit()
for i in range(n):
    if s[i]=="A":
        a+=1
    elif s[i]=="B":
        b+=1
    else:
        c+=1
    if a>=1 and b>=1 and c>=1:
        print(i+1)
        exit()