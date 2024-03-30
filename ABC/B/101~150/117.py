n=int(input())
l=list(map(int,input().split()))

l_max=max(l)
l.remove(l_max)
print("Yes" if sum(l)>l_max else "No")