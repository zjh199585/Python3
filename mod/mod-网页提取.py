import urllib.request

def gethtml(url):
    
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
 
html = gethtml("https://movie.douban.com/people/lingrui1995/collect?start=45&sort=time&rating=all&filter=all&mode=grid")
pageFile=open('/Users/zhuji/Desktop/Python/douban.txt','wb') #以写的方式打开pageCode.txt
pageFile.write(html) #写入
pageFile.close() #开了记得关