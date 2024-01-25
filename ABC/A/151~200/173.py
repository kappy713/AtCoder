n=int(input())
while n>=1000:
    n-=1000
print(n if n==0 else 1000-n)