l=list(map(int,input().split()))
L=set(l)
L=list(L)
if len(L)==1:
    exit(print(L[0]))
print(L[0]*2+L[1]*2-sum(l))