a,b=map(int,input().split())

a_str=str(a)*b
b_str=str(b)*a
print(a_str if a_str<b_str else b_str)