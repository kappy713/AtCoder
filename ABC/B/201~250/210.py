n=int(input())
s=input()

for i in range(n):
    if s[i]=="1" and i%2==0:
        exit(print("Takahashi"))
    elif s[i]=="1" and i%2!=0:
        exit(print("Aoki"))