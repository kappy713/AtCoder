ans=[]
try:
    while True:
        a=int(input())
        ans.append(a)
except EOFError:
    pass
for i in reversed(range(len(ans))):
    print(ans[i])