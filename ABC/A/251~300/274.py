a,b=map(int,input().split())
ans=round(b/a,3)  #round関数で四捨五入(今回の場合は小数部3桁まで表示,すなわち小数点第4位で四捨五入)
print("{:.3f}".format(ans)) #{:.3f}で小数点以下を0埋めしている