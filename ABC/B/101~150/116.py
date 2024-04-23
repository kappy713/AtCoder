s = int(input())

a = [s]
check = {s}
for i in range(1, 10000):
    if a[i-1] % 2 == 0:
        a.append(a[i-1] // 2)
    else:
        a.append(3 * a[i-1] + 1)
    #print(a, check)
    if a[i] in check:
        exit(print(i + 1))
    check.add(a[i])