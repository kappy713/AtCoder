#解説AC,メモ化再帰で計算量をO(logN)orO((logn)^2)にできるため高速
from functools import cache

#Pythonの場合@cacheというデコレータを付けることで自動で再帰関数がメモ化される
@cache
def f(n):
    return 0 if n==1 else f(n//2)+f((n+1)//2)+n

print(f(int(input())))