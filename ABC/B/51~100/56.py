w, a, b = map(int, input().split())

check = b - (a + w)
if check <= 0:
    print(abs(check + a))
else:
    print(check)