a,b = map(int, input().split())

port = 1
ans = 0
while port < b:
    port += a - 1 # 未使用の差込口1口を引く
    ans += 1
#print(port) # 差込口の確認
print(ans)