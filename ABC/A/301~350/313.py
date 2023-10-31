n=int(input())
p=list(map(int,input().split()))
if n==1:
    print(0)
    exit()
max_num=max(p[1:])
ans=max(0,max_num+1-p[0])
print(ans)