import re
a=open(r"/Users/zhuji/Desktop/Python/twitter.txt",'rb')    # rb只读  wb清空写入 ab继续写入
s=a.read()
pattern = re.compile(r'href="(.*)"')
html=s.decode('utf-8')
result1 = pattern.findall(html)
print(result1)
