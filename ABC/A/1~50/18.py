a=int(input())
b=int(input())
c=int(input())

if a<b<c:
    print(3)
    print(2)
    print(1)
elif a<c<b:
    print(3)
    print(1)
    print(2)
elif b<a<c:
    print(2)
    print(3)
    print(1)
elif b<c<a:
    print(1)
    print(3)
    print(2)
elif c<a<b:
    print(2)
    print(1)
    print(3)
elif c<b<a:
    print(1)
    print(2)
    print(3)