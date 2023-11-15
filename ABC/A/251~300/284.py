n=int(input())
ans=[""]*n
for i in range(n):
    s=list(input())
    ans[i]=s
for i in reversed(range(n)):
    print(*ans[i],sep="")