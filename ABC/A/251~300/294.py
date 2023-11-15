n=int(input())
a=list(map(int,input().split()))
ans_list=[]
for i in range(n):
    if a[i]%2==0:
        print(a[i] ,end=" ")