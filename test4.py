import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getimg(html):
    reg = r'href="(*?)">'
    pageFile=open('/Users/嘉皓/Desktop/Python/aaa','wb')
    pageFile.write(reg) 
    pageFile.close() 
html=gethtml("https://movie.douban.com/")
print(getimg(html))
