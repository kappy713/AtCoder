n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=int(input())
c=list(map(int,input().split()))
q=int(input())
x=list(map(int,input().split()))

ans=[]
for i in a:
    for j in b:
        for k in c:
            ans.append(i+j+k)

ans=set(ans)
for z in x:
    if z in ans:
        print("Yes")
    else:
        print("No")