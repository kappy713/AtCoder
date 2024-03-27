n=int(input())
mount={}
for i in range(n):
    s,t=input().split()
    mount[s]=int(t)
ans = sorted(mount.items(), key=lambda x:x[1])
print(ans[-2][0])