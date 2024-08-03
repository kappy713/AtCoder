xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

AB = (xa - xb) ** 2 + (ya - yb) ** 2
BC = (xb - xc) ** 2 + (yb - yc) ** 2
CA = (xc - xa) ** 2 + (yc - ya) ** 2

if AB + BC == CA or BC + CA == AB or AB + CA == BC:
    print('Yes')
else:
    print('No')