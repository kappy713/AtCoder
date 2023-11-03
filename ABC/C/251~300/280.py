s=input()
t=input()

minlen=min(len(s),len(t))

for i in range(minlen):
    if s[i]!=t[i]:
        print(i+1)
        exit()

print(minlen+1)