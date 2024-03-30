s=input()
ans=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        ans.append(s[i:j])

ans_set=set(ans)
ans_set=list(ans_set)
print(len(ans_set))