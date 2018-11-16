d=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            e=a*100+b*10+c
            f=pow(a,3)+pow(b,3)+pow(c,3)
            if e==f:
                d.append(e)
g=len(d)
print(d,'totle:',g)