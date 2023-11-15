n=int(input())
ans=hex(n)  #hex()で10進数を16進数に変換
if len(ans[2:])==1:
    print("0"+ans[2:].upper())
    exit()
print(ans[2:].upper())