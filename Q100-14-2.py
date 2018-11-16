c=[]
for i in range(2,201):
    d=0
    for a in range(2,i):
        if i%a!=0:
            d+=1
            if d==i-2:
                c.append(i)
c.insert(0,2)
z=[]
y=int(input())
for ii in range(45):
    if y%c[ii]==0:
        z.append(c[ii])
        z.append('^')
        for g in range(1,7):
            if y%pow(c[ii],g)==0:
                h=[]
                h.append(g)
        p=max(h)
        z.append(p)
print(z)
print('end')