r, g, b = map(int, input().split())
c = input()

if c == 'Red':
    print(min(g, b))
elif c == 'Blue':
    print(min(r, g))
else:
    print(min(r, b))