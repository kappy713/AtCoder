m=int(input())
d=list(map(int,input().split()))
days=sum(d)
ans_days=(days+1)//2
for i in range(m):
    if ans_days<=d[i]:
        ans_month=i
        print(ans_month+1,ans_days)
        exit()
    else:
        ans_days-=d[i]