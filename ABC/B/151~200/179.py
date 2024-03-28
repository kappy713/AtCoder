n=int(input())
flag=False
cnt=0
for i in range(n):
    d1,d2=map(int,input().split())
    if d1==d2:
        cnt+=1
    else:
        cnt=0
    if cnt>=3:
        flag=True
print("Yes" if flag else "No")