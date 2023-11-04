s=input()
maxnum=0
check=0
for i in range(3):
    if s[i]=="S":
        maxnum=max(maxnum,check)
        check=0
    if s[i]=="R":
        check+=1
print(max(maxnum,check))