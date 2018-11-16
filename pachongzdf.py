import urllib.request
import re
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
html = getHtml("https://movie.douban.com/subject/27605698/?tag=热门&from=gaia_video")
pageFile=open('/Users/zhuji/Desktop/Python/pagex','wb') 
pageFile.write(html) 
pageFile.close() 


    


