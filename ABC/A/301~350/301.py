n=int(input())
s=input()
ans_T=0
ans_A=0
for i in range(n):
    if s[i]=="T":
        ans_T+=1
    if s[i]=="A":
        ans_A+=1
if ans_A==ans_T:
    if s[n-1]=="T":
        print("A")
        exit
    else:
        print("T")
        exit
if ans_T>ans_A:
    print("T")
if ans_T<ans_A:
    print("A")