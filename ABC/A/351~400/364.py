n = int(input())
s = [input() for _ in range(n)]

for i in range(1, n-1):
    if s[i] == 'sweet' and s[i-1] == 'sweet':
        exit(print('No'))
print('Yes')