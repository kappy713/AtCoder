s=input()

maxnum,cnt=0,0
for i in range(len(s)):
    if s[i]=="A" or s[i]=="C" or s[i]=="G" or s[i]=="T":
        cnt+=1
    else:
        maxnum=max(cnt,maxnum)
        cnt=0
print(max(maxnum,cnt))