q=int(input())
query=[list(map(int,input().split())) for _ in range(q)]

a=[]
for i in range(q):
    if query[i][0]==1:
        a.append(query[i][1])
    else:
        print(a[-1*query[i][1]])