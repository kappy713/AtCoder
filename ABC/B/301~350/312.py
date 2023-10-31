n,m=map(int,input().split())
s=[""]*n
for i in range(n):
    s[i]=input()

for i in range(n-8):
    for j in range(m-8):
        if s[i][j:(j+4)] == "###." and s[i+1][j:(j+4)] == "###." and s[i+2][j:(j+4)] == "###." and s[i+3][j:(j+4)] == "....":
            if s[i+5][(j+5):(j+9)] == "...." and s[i+6][(j+5):(j+9)] == ".###" and s[i+7][(j+5):(j+9)] == ".###" and s[i+8][(j+5):(j+9)] == ".###":
                print(i+1,j+1)