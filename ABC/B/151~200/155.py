n=int(input())
a=list(map(int,input().split()))

flag=True
for x in a:
    if x%2==0:
        flag=False
        if x%3==0 or x%5==0:
            flag=True
    if not flag:exit(print("DENIED"))
print("APPROVED")