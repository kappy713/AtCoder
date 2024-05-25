a,b = map(int, input().split())

if a == b:
    exit(print(-1))
    
if a + b == 3:
    print(3)
elif a + b == 4:
    print(2)
elif a + b == 5:
    print(1)
else:
    print(-1)