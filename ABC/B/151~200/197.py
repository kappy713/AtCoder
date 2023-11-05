h,w,x,y=map(int,input().split())
s=[list(input()) for _ in range(h)]
#上下左右の実装,中々大変だけど今回の場合マス自身は考えず行う

ans=0
#マスの右側を探索
for i in range(1,w-y+1):
    if s[x-1][y-1+i]==".":
        ans+=1
    else:
        break

#マスの左側を探索
for j in range(1,y):
    if s[x-1][y-1-j]==".":
        ans+=1
    else:
        break

#マスの下側を探索
for k in range(1,h-x+1):
    if s[x-1+k][y-1]==".":
        ans+=1
    else:
        break

#マスの上側を探索
for l in range(1,x):
    if s[x-1-l][y-1]==".":
        ans+=1
    else:
        break

#マス自身を追加
print(ans+1)