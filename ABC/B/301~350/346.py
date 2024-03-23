w,b=map(int,input().split())

piano="wbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbw"

tmp=w+b
for i in range(len(piano)-tmp):
    if piano[i:i+tmp].count("w")==w and piano[i:i+tmp].count("b")==b:
        exit(print("Yes"))
print("No")