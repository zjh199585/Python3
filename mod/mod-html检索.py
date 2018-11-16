import re

def search(html):
    pattern = re.compile(r'检索开头（.*)检索结尾')
    html = html.decode('utf-8')       #网页读取格式——（utf-8)允许读取汉字
    result = pattern.findall(html)

