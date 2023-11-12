n,q=map(int,input().split())
s=input()
lr=[list(map(int,input().split())) for _ in range(q)]
index_list=[0]*n
for i in range(1,n):
    if s[i-1]==s[i]:
        index_list[i]+=1

for i in range(1,n):
    index_list[i]+=index_list[i-1]

for i in range(q):
    l,r=lr[i]
    l-=1
    r-=1
    ans=index_list[r]-index_list[l]
    print(ans)