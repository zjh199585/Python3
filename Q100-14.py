d=[]
a=int(input())
b=[2,3,5,7,11,13,17,19,21]
for i in range(9):
    if a%b[i]==0:
        d.append(b[i])
        d.append('^')
        for c in range(1,7):
            if a%pow(b[i],c)==0:
                e=[]
                e.append(c)
        f=max(e)
        d.append(f)
print(d)
print('end')
