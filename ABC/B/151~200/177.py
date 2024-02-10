s=input()
t=input()

ans=len(t) #書き換える文字数の最大値
for start in range(len(s)-len(t)+1): #書き換えるスタート位置を探索
    diff=0
    for i in range(len(t)):
        if t[i]!=s[start+i]:
            diff+=1 #sとtが異なれば1回書き換える
    ans=min(ans,diff)
print(ans)