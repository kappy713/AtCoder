s=input()
if s.count("<")==1 and s.count(">")==1 and s[0]=="<" and s[-1]==">" and s.find("="):
    print("Yes")
else:
    print("No")