n=input()

if int(n)<10:
    print("Yes")
else:
    for i in range(1,len(n)):
        if n[i]>=n[i-1]:
            print("No")
            exit()
    print("Yes")