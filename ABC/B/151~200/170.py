x,y=map(int,input().split())

for i in range(x+1):
    for j in range(x+1):
        if i*2+j*4==y and i+j==x:
            print("Yes")
            exit()
print("No")