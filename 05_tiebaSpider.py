"""
    1、输入贴吧名称: 赵丽颖吧
    2、输入起始页: 1
    3、输入终止页: 2
    4、保存到本地文件：赵丽颖吧_第1页.html、赵丽颖吧_第2页.html
"""
import requests
from urllib import parse
import time
import random

class TiebaSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        """请求功能函数"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')

        return html

    def parse_html(self):
        """解析功能函数"""
        pass

    def save_html(self, filename, html):
        """数据处理函数"""
        with open(filename, 'w') as f:
            f.write(html)

    def run(self):
        """程序入口函数"""
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        # 编码
        params = parse.quote(name)
        # 拼接多页的URL地址
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            page_url = self.url.format(params, pn)
            # 请求 + 解析 + 数据处理
            html = self.get_html(url=page_url)
            filename = '{}_第{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 终端提示
            print('第%d页抓取完成' % page)
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()





















