n=int(input())
t=[0]*n
a=[0]*n
for i in range(n):
    t[i],a[i]=input().split()
    a[i]=int(a[i])
ans_index=a.index(min(a))
for i in range(ans_index,n):
    print(t[i])
if ans_index!=0:
    for i in range(0,ans_index):
        print(t[i])