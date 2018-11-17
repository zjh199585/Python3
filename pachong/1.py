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

filmname=[]
filmhtml=[]
filmscore=[]

for i in range(30) :

    html_massage=gethtml(html_b+www)

    last_html=search_html(r'rel="next" href="(.*)"',html_massage)
    www=last_html[0]

    add_filmname=search_html(r'<em>(.*)</em>',html_massage)
    add_filmhtml=search_html(r'a href="(.*)" class=""',html_massage)
    add_filmscore=search_html(r'class="rating(.*?)-t"',html_massage)

    filmname.extend(add_filmname)
    filmhtml.extend(add_filmhtml)
    filmscore.extend(add_filmscore)

    time.sleep(0.5)
    print(filmscore)
    print(len(filmscore))

