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

def text_save(filename, data):#filename为写入文件路径，data为要写入数据列表.
    
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 

html_b='https://movie.douban.com/'
www='people/lingrui1995/collect'

ww=1                                 # 初始键入
filmname=[]
filmhtml=[]
filmscore=[]



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

print(filmname)
print(len(filmname))
print(len(filmscore))

text_save('/Users/zhuji/Desktop/Python/filmscore.txt',filmscore)
text_save('/Users/zhuji/Desktop/Python/filmhtml.txt',filmhtml)

htmlnumber=len(filmhtml)
filmstage=[]
movie_name=[]

for number in range(htmlnumber):
    score=filmscore[number]
    score=float(score)*2.0
    html_massage=gethtml(filmhtml[number])
    add_filmscore2=search_html(r'class="ll rating_num" property="v:average">(.*?)</strong',html_massage)
    add_filmscore2=float(add_filmscore2[0])
    add_filmscore2=add_filmscore2/score

    add_filmstage=search_html(r'span property="v:genre">(.*?)</span',html_massage)
                                                             #大于1为不喜欢，小于1为喜欢
    add_movie_name=search_html(r'v:starring">(.*?)</',html_massage)

    if add_filmscore2 < 1:

        filmstage.extend(add_filmstage)
        movie_name.extend(add_movie_name)

print(filmstage)
print(movie_name)

text_save('/Users/zhuji/Desktop/Python/movie_name.txt',movie_name)
text_save('/Users/zhuji/Desktop/Python/filmstage.txt',filmstage)

print('end')