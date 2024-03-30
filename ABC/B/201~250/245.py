n=int(input())
a=list(map(int,input().split()))

for i in range(2001):
    if i not in a:
        exit(print(i))