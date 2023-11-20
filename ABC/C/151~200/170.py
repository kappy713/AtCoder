x,n=map(int,input().split())
p=list(map(int,input().split()))

for i in range(101):
    if x-i not in p:
        exit(print(x-i))
    if x+i not in p:
        exit(print(x+i))
print(x)