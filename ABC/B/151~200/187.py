n=int(input())
x,y=[],[]
for _ in range(n):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)

cnt=0
for i in range(n):
    for j in range(i+1,n):
        check=(y[j]-y[i])/(x[j]-x[i])
        if -1<=check<=1:
            cnt+=1
print(cnt)