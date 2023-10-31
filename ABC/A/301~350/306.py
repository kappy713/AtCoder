n=int(input())
s=input()
ans=[""]*2*n
for i in range(n):
    ans[2*i]=s[i]
    ans[2*i+1]=s[i]
for i in ans:
    print(i,end="")