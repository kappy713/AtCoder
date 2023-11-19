n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]

ans=[[]for i in range(n)]#[[0]*n]*mだと同じリストを複数入れているため,全て更新されてしまい,想定通りの結果にならない.2次元配列を扱う場合はこちらの書き方の方がいいかも
for i in range(m):
    ans[(ab[i][0])-1].append(ab[i][1])
    ans[(ab[i][1])-1].append(ab[i][0])

for i in range(n):
    ans[i].sort()

for i in range(n):
    print(len(ans[i]), *ans[i])