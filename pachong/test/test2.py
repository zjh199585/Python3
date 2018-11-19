import requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

url = 'https://movie.douban.com/people/lingrui1995/collect'
print(url)
try:
    response=requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        print('可打开')
        a=response.text
        print(a)
except :
    pass
print("end")