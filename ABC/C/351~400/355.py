n, t = map(int, input().split())
a = list(map(int, input().split()))

# 縦, 横, 斜めを別々で管理
row = [0]*n
col = [0]*n
diag = [0, 0]

for i in range(t):
    num = a[i] - 1
    # 商と余りを同時に取得
    q, mod = divmod(num, n)

    row[q] += 1
    col[mod] += 1
    if q == mod:
        diag[0] += 1
    if q + mod == n - 1:
        diag[1] += 1

    if row[q] == n or col[mod] == n or diag[0] == n or diag[1] == n:
        exit(print(i + 1))

print(-1)