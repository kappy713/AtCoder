a,b=map(int,input().split())

for x in range(1,10001):
    if int(x*0.08)==a and int(x*0.1)==b:
        exit(print(x))
print(-1)