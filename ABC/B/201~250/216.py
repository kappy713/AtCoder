n=int(input())
st=[list(input().split()) for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if st[i][0]==st[j][0] and st[i][1]==st[j][1]:
            exit(print("Yes"))
print("No")