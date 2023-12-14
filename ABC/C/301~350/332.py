n,m=map(int,input().split())
S=input()

m_t,l_t=0,0
ans=0
S+="0"
for s in S:
    if s=="0":
        ans=max(ans, max(m_t+l_t-m,l_t))
        m_t,l_t=0,0
    elif s=="1":
        m_t+=1
    elif s=="2":
        l_t+=1
print(ans)