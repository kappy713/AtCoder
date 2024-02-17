a,b,c,d=map(int,input().split())
t=b/a
a=d/c
if t>a:
    print("TAKAHASHI")
elif t<a:
    print("AOKI")
else:
    print("DRAW")