import urllib.request
import re

page = urllib.request.urlopen('https://movie.douban.com/subject/26636712/comments?start=20&limit=20&sort=new_score&status=P')
html = page.read()

pattern = re.compile(r'href="https://www.douban.com/people/(.*)/">')
html=html.decode('utf-8')
result1 = pattern.findall(html)

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 



text_save('/Users/zhuji/Desktop/Python/massage.txt',result1)