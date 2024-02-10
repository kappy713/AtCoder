h,w,n=map(int,input().split())

ans=[["." for _ in range(w)] for _ in range(h)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
angle=0 #向いている角度
h_index=0
w_index=0

for i in range(n):
    if ans[h_index][w_index]==".":
        ans[h_index][w_index]="#"
        angle=(angle+1)%4 #右回転+1
    else:
        ans[h_index][w_index]="."
        angle=(angle-1)%4 #左回転-1
    x=(h_index+dx[angle])%h
    y=(w_index+dy[angle])%w
    h_index=x
    w_index=y
for a in ans:
    print("".join(a))