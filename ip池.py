import requests
from lxml import etree

#反扒
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
#爬取网页
def getHtml(url):
    response = requests.get(url,headers=header)
    response.encoding='utf-8'
    html = response.text
    return html
#解析网页
def parseHtml(html):
    list = []
    html_xpath = etree.HTML(html)
    ip = html_xpath.xpath('//*[@id="ip_list"]//tr/td[2]/text()')
    port = html_xpath.xpath('//*[@id="ip_list"]//tr/td[3]/text()')
    type = html_xpath.xpath('//*[@id="ip_list"]//tr/td[6]/text()')
    for i in range(len(ip)):
        #类型转为小写
        proxy = type[i].lower()+':'+ip[i]+':'+port[i]
        list.append(proxy)
    return list
#测试IP是否可用
def test_ip(ip):
    # 用这个网页去验证，遇到不可用ip会抛异常
    url = "http://2017.ip138.com/ic.asp"
    if ip[:5] == 'https':
        try:
            response = requests.get(url,proxies={'https':ip},timeout=3)
            #可用IP保存到本地
            with open(r'C:\Users\账套\Desktop\ip池.txt','a')as f:
                f.write(ip+'\n')
        except Exception as e:
            print('ip失效')
    else:
        try:
            response = requests.get(url, proxies={'http': ip}, timeout=3)
            with open(r'C:\Users\账套\Desktop\ip池.txt','a')as f:
                f.write(ip+'\n')
        except Exception as e:
            print('ip失效')


if __name__ == "__main__":
    #爬取前5页
    for i in range(1,5):
        url = 'http://www.xicidaili.com/nn/'+str(i)
        html = getHtml(url)
        list = parseHtml(html)
        for ip in list:
            test_ip(ip)

