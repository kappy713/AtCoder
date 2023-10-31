n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(n):
    if a[i]!=ans:
        print("No")
        exit()

print("Yes")