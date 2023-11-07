n=int(input())
k=int(input())

minnum=10**9
for i in range(n+1):
    check=1
    for j in range(n-i,n+1):
        if i+j==n:
            for x in range(i):
                check*=2
            check+=+j*k
        else:
            break
        minnum=min(check,minnum)
print(minnum)