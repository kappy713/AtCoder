n=int(input())
ac,wa,tle,re=0,0,0,0
for i in range(n):
    s=input()
    if s=="AC":
        ac+=1
    elif s=="WA":
        wa+=1
    elif s=="TLE":
        tle+=1
    elif s=="RE":
        re+=1
print(f"AC x {ac}")
print(f"WA x {wa}")
print(f"TLE x {tle}")
print(f"RE x {re}")