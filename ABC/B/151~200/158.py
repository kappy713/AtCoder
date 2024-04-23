n,a,b = map(int, input().split())

base = n // (a + b)
last = n % (a + b)
if last <= a:
    print(base * a + last)
else:
    print(base * a + a)