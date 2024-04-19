n = int(input())
s = list(input().split())

S = set(s)
print("Three" if len(S) == 3 else "Four")