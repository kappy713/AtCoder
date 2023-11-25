d=int(input())

ans=d
for x in range(int(d**0.5)+1): #計算量はO(√D)に収まる
    c=d-x**2
    y=int(c**0.5)
    ans=min(ans,c-y**2,(y+1)**2-c)
print(ans)