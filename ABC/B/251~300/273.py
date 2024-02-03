x,k=map(int,input().split())

for i in range(k):
    x+=0.1
    x=round(x,-1-i) #round()はその値に最も近い数を返す
print(int(x))