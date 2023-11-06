p=int(input())

coin=[1,2,6,24,120,720,5040,40320,362880,3628800,39916800] #11!までの値
for i in range(11):
    if p<coin[i]:
        index=i
        break

ans=0
for x in reversed(range(index)):
    while p>=coin[x]:
        p-=coin[x]
        ans+=1
print(ans)