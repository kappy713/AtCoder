n=int(input())
t=input()
x,y,di=0,0,0
for i in t:
    if i=="S":
        if di==0:x+=1
        elif di==1:y-=1
        elif di==2:x-=1
        elif di==3:y+=1
    else:
        di=(di+1)%4
print(x,y)