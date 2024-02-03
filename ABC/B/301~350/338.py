s=input()
ans="a"
for i in range(ord("b"),ord("z")+1):
    c=chr(i)
    if s.count(c)>s.count(ans):
        ans=c
print(ans)