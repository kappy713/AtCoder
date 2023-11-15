n=int(input())
s=input()
if s.find("|",0)<s.find("*",0) and s.find("*",0)<s.find("|",s.find("|",0)+1):
    print("in")
else:
    print("out")