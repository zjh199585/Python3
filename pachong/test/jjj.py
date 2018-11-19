from urllib import request

url = 'https://movie.douban.com/people/lingrui1995/collect'
  #这是代理IP
ip ='61.138.33.20:808'
  #设置代理ip访问方式，http和https
proxy = {'http':ip,'https':ip}
  #创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
  #创建Opener
opener = request.build_opener(proxy_support)
  #添加User Angent
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
  #安装OPener
request.install_opener(opener)
  #使用自己安装好的Opener
response = request.urlopen(url)
  #读取相应信息并解码
html = response.read().decode("utf-8")
  #打印信息
print(html)