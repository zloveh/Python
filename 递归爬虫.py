import requests
import re
from urllib import parse
import queue
import sys


#设置最大递归深度（默认1000）,不能设置太小，会引发错误
sys.setrecursionlimit(50)
#集合去重
page =set('/item/robots.txt')
#使用队列，便于广度优先
page_1 = queue.Queue()

def recursion(url):
    global page
    response = requests.get(url,headers = header)
    response.encoding='UTF-8'
    html = response.text
    #标题
    title = re.findall(r'<title>(.*?)</title>',html)
    #简介
    #intro = re.findall(r'name="description" content="(.*?)"',html)
    #获取网页中其他词条链接
    urls = re.findall(r'<a target=_blank href="(.*?)"',html)
    print(title[0]+'\n')

    #url去重后放入队列
    for ul in urls[1:]:
        if ul not in page:
            page.add(ul)
            page_1.put(ul)
    #查看队列里面的链接数量
    print(page_1.qsize())
    while True:
        if not page_1.empty():
            new_url = page_1.get()
            ul = 'https://baike.baidu.com' + new_url
            # 递归,捕获因达到最大递归深度而引发的错误
            try:
                recursion(ul)
            except Exception as e:
                break



if __name__ == '__main__':
    #反扒
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    data = parse.quote(input('请输入您要搜索的词条：'))
    url = 'https://baike.baidu.com/item/'+data
    recursion(url)
