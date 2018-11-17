import urllib.request

def gethtml(url):
    
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
 
html = gethtml("https://movie.douban.com/subject/27605698/comments?sort=new_score&status=P")
pageFile=open('/Users/zhuji/Desktop/Python/twitter.txt','wb') #以写的方式打开pageCode.txt
pageFile.write(html) #写入
pageFile.close() #开了记得关