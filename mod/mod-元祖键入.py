def fibonacci(n):
    a,b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a=a+3                           #定义递增变化规律
        counter += 1                    
f = fibonacci(10)                       #定义生成器长度
while True:
    try:
        print (next(f), end=",")
    except StopIteration:
        break