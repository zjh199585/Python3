import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getimg(html):
    reg = r'href="(.*?\.)">(.*?\.)</a>'
    img=re.compile(reg)
    html=html.decode('utf-8')
    imglist=re.findall(img,html)
    x = 0
    for imgurl in imglist:
            pageFile=open('/Users/嘉皓/Desktop/Python/twitter%s'%x,'wb')
            pageFile.write(imgurl)
            pageFile.close() #开了记得关
            x = x+1
html=gethtml("https://movie.douban.com/")
getimg(html)