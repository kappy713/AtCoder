l,r=map(int,input().split())
s=input()

lr=s[l-1:r]
lr_reverse=lr[::-1]
print(s[:l-1]+lr_reverse+s[r:])