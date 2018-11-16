a=[1,2,4,5,6,7,3,4,2]
b=iter(a)
while True:
    try:
        c=next(b)
        if c==3:
            break
        print(c,end=',')  
    except:
        break   
print('1end')
#1##################################### try/except 的使用练习 衔接 break 函数的使用
a=[1,2,4,5,6,7,3,4,2]
b=iter(a)
while True:
    try:
        c=next(b)
        if c==3:
            continue
        print(c,end=',')
    except:
        break
print('2end')
#2#####################################    continue 的使用练习
def fibonacci(x):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > x): 
            return
        yield a
        a+=3
        counter += 1
f = fibonacci(10) 
while True:
    try:
        print (next(f), end=",")
    except StopIteration:
        break
print('3end')
#3#####################################    生成器标准程序
def fibonacci(n):
    c=0
    a=1
    while True :
        if c>n:
            return
        yield a
        a+=3
        c+=1
f=fibonacci(10)
while True:
    try:
        print(next(f),end=',')
    except:
        break
print('4end')
#4#####################################    生成器练习
a=pow(3,0.5)
print(pow(a,3),end=',')
print('5end')
#5######################################    平方函数 pow（x,y)  x底数 指数
def a(x):
    return x+1
b=a(56)
print(b)
#6#######################################      函数定义
a=set('sajdfhasjgfjashf')
print(a)
#7######################################
a=[1,23,0,4,85,4,3,7,8,63]
b=a.pop(2)  
print('pliebiao:',a,b,end=',')
print('end8')
########################################
for a in range(1,100):
    for b in range(1,100):
        if (a+b)*(b-a)==168:
            print(pow(a,2)-100)
print('end')
##########################################
a=int(input('year:'))
b=int(input('morth:'))
c=int(input('day:'))
d=[0,31,60,91,121,152,182,213,244,274,305,335]
e=[0,31,59,90,120,151,181,212,243,273,304,334]
if a%4==0:
    print(d[b-1]+c)
else:
    print(e[b-1]+c)