s = input()

up, low = 0, 0
for c in s:
    if c.isupper():
        up += 1
    else:
        low += 1

if up > low:
    print(s.upper())
else:
    print(s.lower())