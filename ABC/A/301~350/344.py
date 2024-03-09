s=input()
ans=[]
n=0
for i in range(len(s)):
    if s[i]=="|":
        n+=1
        continue
    if n%2==0:ans.append(s[i])
print(*ans,sep="")