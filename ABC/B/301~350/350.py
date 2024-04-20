n,q=map(int,input().split())
t=list(map(int,input().split()))

check = [1] * n
for i in range(q):
    if check[t[i]-1] == 1:
        check[t[i]-1] = 0
    else:
        check[t[i]-1] = 1
print(sum(check))