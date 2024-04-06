n=int(input())

ans={}
for i in range(n):
    a,c=map(int,input().split())
    if c not in ans or a<ans[c]:
        ans[c]=a
print(max(ans.values()))