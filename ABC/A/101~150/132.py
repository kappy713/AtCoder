s=input()
if len(set(s))==2:
    for i in range(ord("A"),ord("Z")+1):
        if s.count(chr(i))==1 or s.count(chr(i))==3:
            exit(print("No"))
    print("Yes")
else:
    print("No")