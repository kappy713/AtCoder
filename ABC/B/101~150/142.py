n,k=map(int,input().split())
h=list(map(int,input().split()))

cnt=0
for x in h:
    if x>=k:
        cnt+=1
print(cnt)