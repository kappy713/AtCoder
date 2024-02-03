M,D=map(int,input().split())
y,m,d=map(int,input().split())

if M==m and D==d:
    print(f"{y+1} 1 1")
elif D==d:
    print(f"{y} {m+1} 1")
else:
    print(f"{y} {m} {d+1}")