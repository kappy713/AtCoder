def check(s,t):
    i=0
    for x in t:
        while i<len(s) and s[i]!=x:
            i+=1
        if i==len(s):
            return False
        i+=1
    return True

s=input().upper()
t=input()
print("Yes" if check(s,t if t[-1]!="X" else t[:-1]) else "No")