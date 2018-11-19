import urllib.request
import re
import time
import random

def gethtml(url):

    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def search_html(massage,html):       # massage 为要检索的信息 以 r'' 表示的内容   html为网页提取的信息

    pattern = re.compile(massage)
    html=html.decode('utf-8')
    result = pattern.findall(html)
    return result

def text_save(filename, data):#filename为写入文件路径，data为要写入数据列表.
    
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()

def text_save2(filename, data):#filename为写入文件路径，data为要写入数据列表.
    
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +' '   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.write('\n')
    file.close()

def txt_reading2(txt):                  # txt为带读取文件地址
    
    with open(txt,'r') as f:
        line = f.read().strip()
        result = re.split(r"[\s\n]", line)
        return result


filmhtml=txt_reading2('/Users/zhuji/Desktop/Python/filmhtml.txt')
filmscore=txt_reading2('/Users/zhuji/Desktop/Python/filmscore.txt')
#for 循环初始化值
htmlnumber=len(filmhtml)
filmstage=[]
movie_name=[]
###############

for number in range(htmlnumber):
    ddf=random.random()
    time.sleep(ddf)

    score=filmscore[number]
    score=float(score)*2.0
    try:
        html_massage=gethtml(filmhtml[number])
        add_filmscore2=search_html(r'class="ll rating_num" property="v:average">(.*?)</strong',html_massage)
        v=['']
        if add_filmscore2 != v :
            add_filmscore2=float(add_filmscore2[0])
        else :
            add_filmscore2=11
        add_filmscore2=add_filmscore2-score
        add_filmstage=search_html(r'span property="v:genre">(.*?)</span',html_massage)
        add_movie_name=search_html(r'v:starring">(.*?)</',html_massage)

        if add_filmscore2 < 0.5 :            #大于1为不喜欢，小于1为喜欢

            text_save2('/Users/zhuji/Desktop/Python/filmstage.txt',add_filmstage)
            fsorce=[]
            fsorce.append(add_filmscore2)
            text_save2('/Users/zhuji/Desktop/Python/filmstage.txt',fsorce)
            text_save('/Users/zhuji/Desktop/Python/movie_name.txt',add_movie_name)

        print(number)


    except:
        pass

print('end')