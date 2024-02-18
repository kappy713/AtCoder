# 解説AC
h,w,n=map(int,input().split())
t=input()
s=[list(input()) for _ in range(h)]

# 海に入らないで移動することができるか
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            continue # 海にいたら次の処理に移る
        I,J=i,j
        flag=True
        for c in t:
            if c=="L":
                J-=1
            elif c=="R":
                J+=1
            elif c=="U":
                I-=1
            else:
                I+=1
            if s[I][J]=="#": # 海に入ったらダメ
                flag=False
                break
        if flag:ans+=1
print(ans)

# 割と愚直な全探索
# マス目を使った問題は苦手だけど, これはそこまで難しくない
# 今回はB問題の方が嫌い