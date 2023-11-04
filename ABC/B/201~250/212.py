x=input()

same,num=True,True
for i in range(3):
    if x[i]!=x[i+1]:
        same=False
    if (int(x[i])+1)%10!=int(x[i+1]):
        num=False
if same or num:
    print("Weak")
else:
    print("Strong")