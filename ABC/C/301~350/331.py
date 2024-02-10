from bisect import bisect
n=int(input())
a=list(map(int,input().split()))

A=sorted(a)
a_sum=[A[0]]*n
for i in range(1,n):
    a_sum[i]=a_sum[i-1]+A[i]

for i in range(n):
    index=bisect(A,a[i])
    print(a_sum[-1]-a_sum[index-1],end=" ")
# 累積和&二分探索