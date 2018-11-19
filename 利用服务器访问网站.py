from urllib import request
import requests

def ip_gethtml(url,ip):
    
    proxy = {'http':ip,'https':ip}    #设置代理ip访问方式，http和https
    proxy_support = request.ProxyHandler(proxy)    #创建ProxyHandler
    opener = request.build_opener(proxy_support)    #创建Opener
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
    request.install_opener(opener)    #安装OPener
    response = request.urlopen(url, timeout=5)    #使用自己安装好的Opener
    html = response.read().decode("utf-8")    #读取相应信息并解码
    return html
ip=['180.168.13.26:8000']
a=ip_gethtml('https://movie.douban.com/people/lingrui1995/collect',ip[0])



import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

with open('/Users/b1ancheng/Desktop/123.txt', 'r') as f:
    for line in f:
        line = line.strip('\n').strip('\ufeff')
        url = 'http://' + line
        print(url)
        try:
            response= requests.get(url, headers=headers, timeout=5).status_code
            print(response)
            if response== 200:
                print('可打开')
            else:
                print(response)
        except Exception as e:
                with open('/Users/b1ancheng/Desktop/1.txt', 'a+') as f1:
                    error = f1.write(line+'\n')
                print(e)