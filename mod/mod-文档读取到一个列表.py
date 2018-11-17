## 把所有文档中的元素载入一个列表，行数据为一个元素
def txt_reading1(txt):                   # txt为带读取文件地址

    with open(txt,'r') as f:
        line = f.readlines()            # 完成列表载入，但是每个项后会存在 '\n'

    g=len(line)
    h=[]
    for i in range(g):
        j=line[i]
        j=j.strip()
        h.append(j)                     # 完成所有元素末尾 '\n' 的消除
    
    print(h)


## 把所有文档中的元素载入一本列表，行数据为分散元素
import re

def txt_reading2(txt):                  # txt为带读取文件地址
    
    with open(txt,'r') as f:
        line = f.read().strip()
        result = re.split(r"[\s\n]", line)
    print(result)