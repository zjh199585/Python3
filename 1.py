import urllib.request
import re
import time
import random
from urllib import request

def ip_gethtml(url,ip):
    
    proxy = {'http':ip,'https':ip}    #设置代理ip访问方式，http和https
    proxy_support = request.ProxyHandler(proxy)    #创建ProxyHandler
    opener = request.build_opener(proxy_support)    #创建Opener
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
    request.install_opener(opener)    #安装OPener
    response = request.urlopen(url)    #使用自己安装好的Opener
    html = response.read()    #读取相应信息并解码
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
    print("保存文件成功") 

# while循环初始化值
html_b='https://movie.douban.com/'
www='people/lingrui1995/collect'
ww=1                                 
filmname=[]
filmhtml=[]
filmscore=[]
################
ip=['210.72.14.142:80','47.104.201.136:53281']
while True :

    html_massage=ip_gethtml(html_b+www,ip[random.randint(0,1)])

    htmlmassage=html_massage.decode('utf-8')
    ww = re.search(r'rel="next" href="(.*)"',htmlmassage)

    add_filmname=search_html(r'a href=".*?" class="">\
                            <em>(.*?)</em>[\s\S]*?"rating.-t"',html_massage)              #跨行万能关联 [\s\S]*? 差一行尽量复制加\
    add_filmhtml=search_html(r'a href="(.*?)" class="">\
                            <em>.*</em>[\s\S]*?"rating.-t"',html_massage)
    add_filmscore=search_html(r'a href=".*?" class="">\
                            <em>.*</em>[\s\S]*?"rating(.)-t"',html_massage)

    filmscore.extend(add_filmscore)
    filmname.extend(add_filmname)
    filmhtml.extend(add_filmhtml)
    
    print(filmname)
    print(len(filmname))
    print(len(filmscore))
    if ww == None:
        break
    www=ww.group(1)

text_save('/Users/LAAAAA~/Desktop/Python程序/filmscore.txt',filmscore)
text_save('/Users/LAAAAA~/Desktop/Python程序/filmhtml.txt',filmhtml)

#for 循环初始化值
htmlnumber=len(filmhtml)
filmstage=[]
movie_name=[]
###############

for number in range(htmlnumber):


    score=filmscore[number]
    score=float(score)*2.0
    html_massage=ip_gethtml(filmhtml[number],ip[random.randint(0,1)])
    add_filmscore2=search_html(r'class="ll rating_num" property="v:average">(.*?)</strong',html_massage)
    v=['']
    if add_filmscore2 != v :
        add_filmscore2=float(add_filmscore2[0])
    else :
        add_filmscore2=0
    add_filmscore2=add_filmscore2/score
    add_filmstage=search_html(r'span property="v:genre">(.*?)</span',html_massage)
    add_movie_name=search_html(r'v:starring">(.*?)</',html_massage)

    if add_filmscore2 < 1:            #大于1为不喜欢，小于1为喜欢

        filmstage.extend(add_filmstage)
        movie_name.extend(add_movie_name)
    print(filmstage)
    print(number)

text_save('/Users/LAAAAA~/Desktop/Python程序/movie_name.txt',movie_name)
text_save('/Users/LAAAAA~/Desktop/Python程序/filmstage.txt',filmstage)

print('end')