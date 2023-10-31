s=list(map(int,input().split()))
for i in range(len(s)):
    if i==0 and 100<=s[i]<=675 and s[i]%25==0:
        continue
    if 100<=s[i]<=675 and s[i]%25==0 and s[i-1]<=s[i]:
        continue
    else:
        print("No")
        exit()
print("Yes")