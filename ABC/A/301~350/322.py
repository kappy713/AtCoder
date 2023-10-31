n=int(input())
s=input()

for i in range(2,n):
    if s[i]=="C" and s[i-1]=="B" and s[i-2]=="A":
        print(i-1)
        exit()
print(-1)