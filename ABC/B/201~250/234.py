import numpy as np

n=int(input())
X,Y=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

maxnum=0
for i in range(n):
    for j in range(i+1,n):
        tmp=np.sqrt((X[j]-X[i])**2+(Y[j]-Y[i])**2)
        maxnum=max(maxnum,tmp)
print(maxnum)