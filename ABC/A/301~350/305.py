n=int(input())
a=n%10
if 0<=a<=2 or 8<=a:
    ans=n-a
elif 3<=a<=7:
    ans=(n-a)+5
else:
    pass
print(ans)