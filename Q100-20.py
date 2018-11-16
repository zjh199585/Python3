a=int(input('ldcs:'))
b=100
c=0
if a>1:
    for i in range(2,a+1):
        c=c+b/(pow(2,i-2))
    c+=100
else:
    c=100
print(c)