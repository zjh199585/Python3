import urllib.request
import re
import time

def gethtml(url):

    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def search_html(massage,html):       # massage 为要检索的信息 以 r'' 表示的内容   html为网页提取的信息

    pattern = re.compile(massage)
    html=html.decode('utf-8')
    result = pattern.findall(html)
    return result

html_b='https://movie.douban.com/'
www='people/lingrui1995/collect'

ww=1                                 # 初始键入
filmname=[]
filmhtml=[]
filmscore=[]

while True :

    html_massage=gethtml(html_b+www)

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
    

    time.sleep(0.5)
    print(filmname)
    print(len(filmname))
    print(len(filmscore))
    if ww == None:
        break
    www=ww.group(1)

print('end')