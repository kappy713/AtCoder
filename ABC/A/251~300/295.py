n=int(input())
w=input().split()
for i in range(n):
    if w[i]=="and" or w[i]=="not" or w[i]=="that" or w[i]=="the" or w[i]=="you":
        print("Yes")
        exit()
print("No")