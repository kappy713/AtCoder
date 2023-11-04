n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans1,ans2=0,0
for i in range(n):
    for j in range(n):
        if a[i]==b[j] and i==j:
            ans1+=1
        if a[i]==b[j] and i!=j:
            ans2+=1
print(ans1)
print(ans2)