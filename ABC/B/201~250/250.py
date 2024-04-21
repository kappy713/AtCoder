n, a, b = map(int, input().split())

for i in range(n):
    for j in range(a):
        for k in range(n):
            if (k % 2 == 0 and i % 2 == 0) or (k % 2 == 1 and i % 2 == 1):
                print("."*b, end = "")
            else:
                print("#"*b, end = "")
        print()