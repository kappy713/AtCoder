n=int(input())
s=input()

ans=[0]*26
strsum=1
for i in range(n-1):
    check=ord(s[i])-97
    if s[i]==s[i+1]:
        strsum+=1
    else:
        ans[ord(s[i])-97]=max(ans[ord(s[i])-97],strsum)
        strsum=1
ans[ord(s[n-2])-97]=max(ans[ord(s[n-2])-97],strsum)
if len(set(s))>sum(ans):
    print(len(set(s)))
else:
    print(sum(ans))