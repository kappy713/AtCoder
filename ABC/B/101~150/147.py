s=input()

n=len(s)
ans=0
for i in range(n//2): #「n//2」の理由回文のため真ん中を対称にし,比較
    if s[i]!=s[n-i-1]:
        ans+=1
print(ans)