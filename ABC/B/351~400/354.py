n = int(input())

check = {}
sum_rate = 0
for _ in range(n):
    s,c = input().split()
    sum_rate += int(c)
    check[s] = int(c)

res = dict(sorted(check.items()))
num = sum_rate%n
check_list = list(res)
print(check_list[num])