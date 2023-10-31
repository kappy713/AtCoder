n,m=map(int,input().split())
a_list,b_list=[],[]
ans_b=[0]*n
if m==0:
    print(-1)
    exit()
for _ in range(m):
    a,b=map(int,input().split())
    a_list.append(a)
    b_list.append(b)

for i in range(m):
    for j in range(n):
        if b_list[i]==j+1:
            ans_b[b_list[i]-1]+=1 
j=0
for i in range(n):
    if j>1:
        print(-1)
        exit()
    if ans_b[i]==0:
        ans=i+1
        j+=1
print(ans)