s, t = input().split()

for w in range(1, len(s)):
    for i in range(w):
        if s[i::w] == t:
            exit(print('Yes'))
print('No')