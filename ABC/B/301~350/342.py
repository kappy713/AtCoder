n=int(input())
p=list(map(int,input().split()))
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    print(a if p.index(a)<p.index(b) else b)