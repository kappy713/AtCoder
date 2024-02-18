# 解説AC
n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    s,t=map(int,input().split())
    a[i+1]+=a[i]//s*t
print(a[-1])

# a[i]はs[i]以上の時にしか操作ができないため、操作回数は必然的にa[i]//s[i]回となる
# a[i+1]はその回数だけt[i]が加算されるため、tをかける
# これをn-1回繰り返すとa[n-1]の最大値が求まる
# 操作を全部求めると時間がかかるため、それぞれの配列では何回操作を行うのかを考える