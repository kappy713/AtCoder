contest=["ABC","ARC","AGC","AHC"]
s=[]
s.append(input())
s.append(input())
s.append(input())

miss=set(contest)-set(s) #setに変換して差を取る
print(list(miss)[0])