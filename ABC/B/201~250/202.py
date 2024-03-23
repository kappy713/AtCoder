s=input()

ans=[]
for x in s:
    if x=="6":
        ans.append("9")
    elif x=="9":
        ans.append("6")
    else:
        ans.append(x)
for i in reversed(ans):
    print(i,end="")