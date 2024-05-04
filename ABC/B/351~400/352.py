s = input()
t = input()

ans = []
i = 0
for j in range(len(t)):
    if s[i] == t[j]:
        ans.append(j+1)
        i += 1
for x in ans:
    print(x,end=" ")