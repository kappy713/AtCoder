n=int(input())

N=bin(n) #nを2進数に変換
N=N[::-1] #リスト(文字列)を反転
ans=0
for i in range(len(N)-2):
    if N[i]=="1": #頭から探索して1が見つかったらそれまでの0の個数を出力
        break
    ans+=1
print(ans)