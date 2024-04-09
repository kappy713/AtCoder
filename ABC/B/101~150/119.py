n=int(input())
jp,bt=0,0
for i in range(n):
    x,y=input().split()
    if y=="JPY":
        jp+=float(x)
    else:
        bt+=float(x)
print(jp+(bt*380000))