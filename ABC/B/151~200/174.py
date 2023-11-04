import numpy as np

n,d=map(int,input().split())
X,Y=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

ans=0
for i in range(n):
    z=np.sqrt(np.power(X[i],2)+np.power(Y[i],2))
    if z<=d:
        ans+=1
print(ans)