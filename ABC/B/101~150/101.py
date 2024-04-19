n = input()

n_sum = 0
for c in n:
    n_sum += int(c)

print("Yes" if int(n) % n_sum == 0 else "No")