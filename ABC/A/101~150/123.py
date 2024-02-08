a=[list(map(int,input().split())) for _ in range(5)]
k=int(input())
for i in range(5):
    for j in range(i+1,5):
        if a[j][0]-a[i][0]>k:
            exit(print(":("))
print("Yay!")