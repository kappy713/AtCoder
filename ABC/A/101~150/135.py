a,b=map(int,input().split())
k=max(a,b)-min(a,b)
if (k/2)%1==0:
    exit(print(min(a,b)+(k//2)))
print("IMPOSSIBLE")