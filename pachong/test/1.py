import urllib.request
import re
import time
import random
import requests

keys = [

    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',

    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',

    'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',

    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',

    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',

    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',

    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',

    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',

    'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'

]
headers = {'User-Agent': keys[random.randint(0, len(keys) - 1)]}

def getXCProxyIp(url):


    for i in range(1, 10):

        page_number = i

        init_url = 'http://www.xicidaili.com/nn/' + str(i)

        req = requests.get(init_url, headers=headers)

        # 获取代理ip

        agency_ip_re = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' ,re.S)

        agency_ip = agency_ip_re.findall(req.text)

        # 获取代理ip的端口号

        agency_port_re = re.compile('<td>([0-9]{2,5})</td>', re.S)

        agency_port = agency_port_re.findall(req.text)

        # 高匿代理ip页面中所列出的ip数量

        ip_number = len(agency_ip)

        print('正在获取第 %d 页代理中（请耐心等候）......' % page_number)

        for i in range(ip_number):

            total_ip = agency_ip[i] + ':' + agency_port[i]
            print(total_ip)
            proxies = {'http':total_ip,'https':total_ip}    #设置代理ip访问方式，http和https

            try:
                response = requests.get(url,headers=headers,proxies=proxies,timeout=5)    #使用自己安装好的Opener

                if response.status_code == 200 :
                    html5=response.text
                    print(i,'yes')
                return html5   

            except:
                print(i,'try')
                pass
                
        print(i,'页没有')

def search_html(massage,html):       # massage 为要检索的信息 以 r'' 表示的内容   html为网页提取的信息

    pattern = re.compile(massage)
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

# while循环初始化值
html_b='https://movie.douban.com/'
www='people/lingrui1995/collect'
ww=1                                 
filmname=[]
filmhtml=[]
filmscore=[]
################

while True :

    html_massage=getXCProxyIp(html_b+www)

    ww = re.search(r'rel="next" href="(.*)"',html_massage)

    add_filmname=search_html(r'a href=".*?" class="">\
                            <em>(.*?)</em>[\s\S]*?"rating.-t"',html_massage)              #跨行万能关联 [\s\S]*? 差一行尽量复制加\
    add_filmhtml=search_html(r'a href="(.*?)" class="">\
                            <em>.*</em>[\s\S]*?"rating.-t"',html_massage)
    add_filmscore=search_html(r'a href=".*?" class="">\
                            <em>.*</em>[\s\S]*?"rating(.)-t"',html_massage)

    filmscore.extend(add_filmscore)
    filmname.extend(add_filmname)
    filmhtml.extend(add_filmhtml)

    ddf=random.random()
    time.sleep(ddf)

    print(filmname)
    print(len(filmname))
    print(len(filmscore))
    if ww == None:
        break
    www=ww.group(1)

text_save('/Users/zhuji/Desktop/Python/filmscore.txt',filmscore)
text_save('/Users/zhuji/Desktop/Python/filmhtml.txt',filmhtml)

#for 循环初始化值
htmlnumber=len(filmhtml)
filmstage=[]
movie_name=[]
###############

for number in range(htmlnumber):
    ddf=random.random()
    time.sleep(ddf)

    score=filmscore[number]
    score=float(score)*2.0
    try:
        html_massage=getXCProxyIp(filmhtml[number])
        add_filmscore2=search_html(r'class="ll rating_num" property="v:average">(.*?)</strong',html_massage)
        v=['']
        if add_filmscore2 != v :
            add_filmscore2=float(add_filmscore2[0])
        else :
            add_filmscore2=0
        add_filmscore2=add_filmscore2/score
        add_filmstage=search_html(r'span property="v:genre">(.*?)</span',html_massage)
        add_movie_name=search_html(r'v:starring">(.*?)</',html_massage)

        if add_filmscore2 < 1:            #大于1为不喜欢，小于1为喜欢

            filmstage.extend(add_filmstage)
            movie_name.extend(add_movie_name)
        print(filmstage)

        text_save('/Users/zhuji/Desktop/Python/movie_name.txt',movie_name)
        text_save('/Users/zhuji/Desktop/Python/filmstage.txt',filmstage)
    except:
        pass

print('end')