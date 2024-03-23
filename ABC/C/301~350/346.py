n,k=map(int, input().split())
a=list(map(int, input().split()))

a_set=set(x for x in a if 1<=x<=k)
a_sum=sum(a_set)
miss_sum=(k*(k+1))//2-a_sum #1~kの総和=(k*(k+1))//2
print(miss_sum)