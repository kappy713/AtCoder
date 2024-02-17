s=input()
n=int(input())
x=[]
for i in s:
    for j in s:
        x.append(i+j)
print(x[n-1])