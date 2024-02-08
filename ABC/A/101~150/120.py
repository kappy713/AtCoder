a,b,c=map(int,input().split())
if a*c<=b:
    print(c)
elif a>b:
    print(0)
else:
    print(b//a)