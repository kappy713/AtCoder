n=input()

for i in range(10):
    tmp="0"*i+n
    if tmp==tmp[::-1]:
        exit(print("Yes"))
print("No")