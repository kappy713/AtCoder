h,m = map(int, input().split())

while True:
    if m == 60:
        h = (h+1)%24
        m = 0
    a,b = h//10,h%10
    c,d = m//10,m%10
    if 0 <= a*10+c < 24 and 0 <= b*10+d < 60:
        exit(print(h, m))
    m += 1