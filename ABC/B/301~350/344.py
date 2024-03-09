ans=[]
while True:
    n=int(input())
    ans.append(n)
    if n==0:
        break
for i in reversed(range(len(ans))):
    print(ans[i])