n=int(input())

for i in range(1,61):
    if 2**i>n:
        exit(print(i-1))