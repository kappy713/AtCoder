n=int(input())

n_sum=0
for i in range(1,n+1):
    if not(i%3==0 or i%5==0):
        n_sum+=i
print(n_sum)