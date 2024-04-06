from collections import Counter
n=int(input())

ab=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    ab.append(a)
    ab.append(b)
counter=Counter(ab)
maxnum=counter.most_common(1)[0][0]
check=0
for i in range(0,len(ab),2):
    if ab[i]==maxnum:
        check+=ab[i+1]
    elif ab[i+1]==maxnum:
        check+=ab[i]
    else:
        exit(print("No"))
sum_n=n*(n+1)//2
print("Yes" if sum_n-maxnum==check else "No")