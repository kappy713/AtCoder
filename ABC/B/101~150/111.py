n=int(input())

if n%111==0:
    print(n)
else:
    tmp=(n//111)+1
    print(111*tmp)