n,k=map(int,input().split())

for i in range(k):
    if n%200==0:
        n//=200
    else:
        tmp=str(n)+"200"
        n=int(tmp)
print(n)