n,d=map(int,input().split())
s=[]
for _ in range(n):
    s.append(input())

count=0
ans=[0]
flag=False
for j in range(d):
    if s[0][j]=="o":
        flag=True
        for i in range(n):
            if s[i][j]!="o":
                flag=False
                ans.append(count)
                count=0
                break
        if flag:
            count+=1
    else:
        flag=False
        ans.append(count)
        count=0 
ans.append(count)   
print(max(ans))