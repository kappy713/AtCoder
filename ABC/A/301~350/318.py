n,m,p=map(int,input().split())

n-=m
count=0
while n>=0:
    n-=p
    count+=1
print(count)