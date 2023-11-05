a,b=input().split()

ab=a+b
ab=int(ab)
for i in range(1,317): #今回の場合316*316=99856が最大
    if i*i==ab:
        print("Yes")
        exit()
print("No")