a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(a) - sum(b) + 1
print(ans)