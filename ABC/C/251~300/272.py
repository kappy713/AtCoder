n=int(input())
a=list(map(int,input().split()))

a.sort()
even,odd=[],[]
for x in a:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

ans=-1
if len(even)>=2:
    ans=max(ans,even[-1]+even[-2])
if len(odd)>=2:
    ans=max(ans,odd[-1]+odd[-2])
print(ans)