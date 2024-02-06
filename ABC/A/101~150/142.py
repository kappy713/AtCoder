n=int(input())
tmp=0
for i in range(1,n+1):
    if i%2!=0:
        tmp+=1
print(tmp/n)