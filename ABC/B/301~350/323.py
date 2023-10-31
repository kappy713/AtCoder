n=int(input())
S=[]
for i in range(n):
    s=input()
    S.append(s)

sumlist=[0]*n

for i in range(n):
    for j in range(n):
        if S[i][j]=="o":
            sumlist[i]+=1

ans=[]
for i in range(n):
    ans.append(sumlist.index(max(sumlist))+1)
    sumlist[sumlist.index(max(sumlist))]=-1
print(*ans)