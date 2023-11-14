import math

abcde=[int(input()) for _ in range(5)]

ans=0
amari=[]
for i in range(5):
    num=abcde[i]
    if num%10!=0:
        amari.append(num%10)
    ans+=10*(math.ceil(num/10)) #math.ceilで小数点以下を切り上げ,整数で返される
if len(amari)==0:
    print(ans)
else:
    print(ans-10+min(amari))