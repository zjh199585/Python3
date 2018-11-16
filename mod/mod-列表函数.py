a=len(list)                  #返回列表 list 中的元素总数

a=max(list)                  #返回列表 list 中的最大值

a=min(list)                  #返回列表 list 中的最小值

list.append(a)               #在列表末尾添加元素 a

b=list.count(a)              #统计某个元素在列表中出现的次数

list.extend(list1)           #在列表末尾添加列表 list1 的数值

list.index(a)                #从列表中找出 a 第一个匹配项的索引位置

list.insert(index, a)        #在 index 位置插入一个值 a

list.pop(index)              #删除列表中 index 位置的一个值，默认为最后一位

list.remove(a)               #移除列表中第一个值为 a 的项

list.reverse()               #把 list 倒序排列

list.sort(cmp=None, key=None, reverse=False)        
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse = True 降序， reverse = False 升序

list.clear                   #清空列表

list1=list.copy()            #复制列表