import re

def search_html(massage,html):       # massage 为要检索的信息 以 r'' 表示的内容   html为网页提取的信息

    pattern = re.compile(massage)
    html=html.decode('utf-8')
    result = pattern.findall(html)
    return result