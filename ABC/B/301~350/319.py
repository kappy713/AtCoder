n=int(input())

s=[]
for i in range(n+1):
    a=[]
    for j in range(1,10):
        if (n%j==0 and i%(n//j)==0):
            a.append(j)
    if a==[]:
        s.append("-")
        continue
    s.append(min(a))
for i in range(n+1):
    print(s[i],end="")