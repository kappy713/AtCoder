n=input()

for x in range(int(n),920):
    X=str(x)
    if int(X[0])*int(X[1])==int(X[2]):
        break

print(X) 