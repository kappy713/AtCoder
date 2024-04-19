s = input()
t = input()

for i in range(26):
    s2 = ''.join(chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in s)
    if s2 == t:
        print("Yes")
        break
else:
    print("No")