n=int(input())
a=str(n)
if len(a)<=3:
    print(n)
    exit()
if len(a)==4:
    print(a[:-1]+"0")
    exit()
if len(a)==5:
    print(a[:-2]+"00")
    exit()
if len(a)==6:
    print(a[:-3]+"000")
    exit()
if len(a)==7:
    print(a[:-4]+"0000")
    exit()
if len(a)==8:
    print(a[:-5]+"00000")
    exit()
if len(a)==9:
    print(a[:-6]+"000000")
    exit()