n, l = map(int, input().split())

apple = [l + i - 1 for i in range(1, n+1)]
apple_sum = sum(apple)
if 0 in apple:
    pass
else:
    if abs(apple[0]) < abs(apple[-1]):
        apple.pop(0)
    else:
        apple.pop(-1)
ans = sum(apple)
print(ans)