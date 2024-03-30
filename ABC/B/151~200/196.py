x=input()
if "." in x:
    point_index=x.index(".")
    print(x[:point_index])
else:
    print(x)