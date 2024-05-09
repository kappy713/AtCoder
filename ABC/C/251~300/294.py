n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a + b)

for x in a:
    print(c.index(x) + 1,end=" ")
print(sep="")
for x in b:
    print(c.index(x) + 1,end=" ")