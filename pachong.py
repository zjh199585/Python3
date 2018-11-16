import urllib.request
#print(urllib.__file__)
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
 
html = getHtml("http://www.baidu.com")
pageFile=open('/Users/zhuji/Desktop/Python/twitter.txt','wb') #以写的方式打开pageCode.txt
pageFile.write(html) #写入
pageFile.close() #开了记得关