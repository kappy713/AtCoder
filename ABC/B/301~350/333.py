s=input()
t=input()

a="ABCDE"
s1=a.index(s[0])
s2=a.index(s[1])
t1=a.index(t[0])
t2=a.index(t[1])

dis_s=abs(s1-s2)
dis_t=abs(t1-t2)
ans="No"
if (dis_s == 1 or dis_s == 4) == (dis_t == 1 or dis_t == 4):
    ans="Yes"
print(ans)