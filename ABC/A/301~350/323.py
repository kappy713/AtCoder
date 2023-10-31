s=input()
for i in range(1,17):
    if (i+1)%2!=0:
        continue
    if int(s[i])%2!=0:
        print("No")
        exit()
print("Yes")