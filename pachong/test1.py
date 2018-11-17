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
www='people/lingrui1995/collect?start=2670&sort=time&rating=all&filter=all&mode=grid'

filmname=[]
filmhtml=[]
filmscore=[]


html_massage=gethtml(html_b+www)

html_massage=html_massage.decode('utf-8')
ww = re.search(r'rel="next" href="(.*)"',html_massage)

print(ww)
print(1)

