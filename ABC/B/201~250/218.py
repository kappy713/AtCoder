p=list(map(int,input().split()))

eng=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans=[]
for x in p:
    ans.append(eng[x-1])
print("".join(ans))