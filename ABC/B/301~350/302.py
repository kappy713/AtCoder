h,w=map(int,input().split())
s=[input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=="s":
            # 横に並ぶ場合(左から右へ)
            if j+4<w:
                if s[i][j+1]=="n" and s[i][j+2]=="u" and s[i][j+3]=="k" and s[i][j+4]=="e":
                    i+=1
                    j+=1
                    for x in range(5):
                        print(i,j+x)
                    exit()
            # 縦に並ぶ場合(上から下へ)
            if i+4<h:
                if s[i+1][j]=="n" and s[i+2][j]=="u" and s[i+3][j]=="k" and s[i+4][j]=="e":
                    i+=1
                    j+=1
                    for x in range(5):
                        print(i+x,j)
                    exit()
            # 斜め右下に並ぶ場合(↘)
            if i+4<h and j+4<w:
                if s[i+1][j+1]=="n" and s[i+2][j+2]=="u" and s[i+3][j+3]=="k" and s[i+4][j+4]=="e":
                    i+=1
                    j+=1
                    for x in range(5):
                        print(i+x,j+x)
                    exit()
            #斜め右上に並ぶ場合(↗)
            if i-4>=0 and j+4<w:
                if s[i-1][j+1]=="n" and s[i-2][j+2]=="u" and s[i-3][j+3]=="k" and s[i-4][j+4]=="e":
                    i+=1
                    j+=1
                    for x in range(5):
                        print(i-x,j+x)
                    exit()

# sの文字列を反転させる,上と逆の操作を行う
tmp=[]
for datas in s[::-1]:
    tmp.append(datas[::-1])

s = tmp

for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            # 横に並ぶ場合(右から左へ)
            if j+4<w:
                if s[i][j+1]== "n" and s[i][j+2]=="u" and s[i][j+3]=="k" and s[i][j+4]=="e":
                    i=h-i
                    j=w-j
                    for x in range(5):
                        print(i,j-x)
                    exit()
            # 縦に並ぶ場合(下から上へ)
            if i+4<h:
                if s[i+1][j]=="n" and s[i+2][j]=="u" and s[i+3][j]=="k" and s[i+4][j]=="e":
                    i=h-i
                    j=w-j
                    for x in range(5):
                        print(i-x,j)
                    exit()
            # 斜め左下に並ぶ場合(↙)
            if i+4<h and j+4<w:
                if s[i+1][j+1]=="n" and s[i+2][j+2]=="u" and s[i+3][j+3]=="k" and s[i+4][j+4]=="e":
                    i=h-i
                    j=w-j
                    for x in range(5):
                        print(i-x,j-x)
                    exit()

            # 斜め左上に並ぶ場合(↖)
            if i-4>=0 and j+4<w:
                if s[i-1][j+1]=="n" and s[i-2][j+2]=="u" and s[i-3][j+3]=="k" and s[i-4][j+4]=="e":
                    i=h-i
                    j=w-j
                    for x in range(5):
                        print(i+x,j-x)
                    exit()