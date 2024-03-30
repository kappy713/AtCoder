n=int(input())
s=[input() for _ in range(n)]

s_set=set(s)
s_set=list(s_set)

s_max=(0,"")
for j in range(len(s_set)):
    cnt=s.count(s_set[j])
    if cnt>s_max[0]:
        s_max=(cnt,s_set[j])
print(s_max[1])