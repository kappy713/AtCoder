n=int(input())
s=list(input())

flag=True
for i in range(n):
    if flag and s[i]==",":
        s[i]="."
    elif flag and s[i]=='"':
        flag=False
    elif not flag and s[i]=='"':
        flag=True
    
print(*s,sep="")