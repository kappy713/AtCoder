n=int(input())
S=[]
for _ in range(n):
    s=input()
    S.append(s)
#print(S)

for i in range(n):
    for j in range(n):
        if i!=j:
            ans=S[i]+S[j] #文字列を連結
            if ans==ans[::-1]: #ans[::-1]で,結合した文字列を反転させる(逆順にする)
                print("Yes")
                exit()
print("No")