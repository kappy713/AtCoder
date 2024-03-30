a,b=input().split()

for i in range(1,min(len(a),len(b))+1):
    if int(a[-1*i])+int(b[-1*i])>=10:
        exit(print("Hard"))
print("Easy")