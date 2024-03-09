n=int(input())
ans=[]
for x in range(1,n+1):
    if x**3>n:
        break
    if str(x**3)==str(x**3)[::-1]:
        ans.append(x**3)
print(ans[-1])