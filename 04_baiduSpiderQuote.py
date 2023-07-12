"""
    终端输入搜索关键字,保存响应内容到本地文件
"""
import requests
from urllib import parse

# 1. 拼接URL地址
word = input('请输入搜索关键字:')
params = parse.quote(word)
url = 'http://www.baidu.com/s?wd={}'.format(params)

# 2. 发请求获取响应内容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html = requests.get(url=url, headers=headers).content.decode('utf-8')

# 3. 保存到本地文件
filename = '{}.html'.format(word)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)






















