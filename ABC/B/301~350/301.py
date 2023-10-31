n=int(input())
a=list(map(int,input().split()))

A=[]
for i in range(1,n):
    if abs(a[i-1]-a[i])==1:
        A.append(a[i-1])
        continue
    else:
        if a[i-1]<a[i]:
            A.append(a[i-1])
            for j in range(1,a[i]-a[i-1]):
                A.append(a[i-1]+j)
        elif a[i-1]>a[i]:
            A.append(a[i-1])
            for j in range(1,a[i-1]-a[i]):
                A.append(a[i-1]-j)
A.append(a[-1])
print(*A)