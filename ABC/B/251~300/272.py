n,m = map(int, input().split())
check = [[0 for i in range(n)] for j in range(n)]

for x in range(m):
    kx = list(map(int, input().split()))
    for i in range(1,kx[0]+1):
        for j in range(1,kx[0]+1):
            check[kx[i]-1][kx[j]-1] = 1
print("No" if any(0 in row for row in check) else "Yes")