c=[]
for i in range(2,201):
    d=0
    for a in range(2,i):
        if i%a!=0:
            d+=1
            if d==i-2:
                c.append(i)
e=len(c)
print(c)
print('totle:',end=' ')
print(e)
print('end')