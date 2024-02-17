x,a,b=map(int,input().split())
if b-a<=0:
    print("delicious")
else:
    if b-a<=x:
        print("safe")
    else:
        print("dangerous")