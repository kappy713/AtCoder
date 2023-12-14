k,g,m=map(int,input().split())
G,M=0,0

while k>0:
    if G==g:
        G=0
    elif M==0:
        M=m
    else:
        while M>0 and G<g:
            M-=1
            G+=1
    k-=1
print(G,M)