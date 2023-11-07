a,b,c=map(int,input().split())
k=int(input())

abc_list=[]
abc_list.append(a)
abc_list.append(b)
abc_list.append(c)
abc_list.sort()

for i in range(k):
    abc_list[-1]*=2
print(sum(abc_list))