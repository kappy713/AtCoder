n,m=map(int,input().split())
a=list(map(int,input().split()))

maxlist=(0,0) #(候補者, 投票数)
check=[0]*(n+1)

for i in range(m):
    check[a[i]]+=1
    if maxlist[1]<check[a[i]]: #投票数をプラス
        maxlist=(a[i],check[a[i]])
    elif maxlist[1]==check[a[i]] and maxlist[0]>a[i]: #投票数が同じ場合番号が若い人を出力
        maxlist=(a[i],check[a[i]])
    print(maxlist[0])