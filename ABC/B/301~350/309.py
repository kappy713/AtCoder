n=int(input())
a=[input() for _ in range(n)]
ans=[[""]*n for i in range(n)]
#print(a,ans)

for i in range(n):
    for j in range(n):
        if i==0 and j<n-1:
            ans[i][j+1]=a[i][j]
        elif i<n-1 and j==n-1:
            ans[i+1][j]=a[i][j]
        elif i==n-1 and j>0:
            ans[i][j-1]=a[i][j]
        elif i>0 and j==0:
            ans[i-1][j]=a[i][j]
        else:
            ans[i][j]=a[i][j]

for i in range(n):
    print("".join(ans[i]))