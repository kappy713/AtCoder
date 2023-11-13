n=int(input())
a=list(map(int,input().split()))

p=0
check_list=[0]*4
for i in range(n):
    check_list[0]=1
    next_check_list=[0]*4
    for j in range(4):
        if check_list[j]==1:
            if j+a[i]>=4:
                p+=1
            else:
                next_check_list[j+a[i]]=1
    check_list=next_check_list
print(p)