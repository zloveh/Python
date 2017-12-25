import DataOutput
import HtmlDownloader
import HtmlParser
import URLManager

class SpiderMan(object):
    def __init__(self):
        self.manager=URLManager.UrlManager()
        self.downloader=HtmlDownloader.HtmlDownloader()
        self.parser=HtmlParser.HtmlParser()
        self.output=DataOutput.DataOutput()
    def crawl(self,root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断URL管理器中是否有新的url,同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            #try:
                #从url管理器获取新的url
                new_url=self.manager.get_new_url()
                #html下载器下载网页
                html=self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls,data=self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取%s个链接'%self.manager.old_url_size())
            #except Exception as e:
             #   print('crawl failed')
        #数据存储器将文件输出成指定格式
        self.output.output_html()
if __name__=='__main__':
    spider_man=SpiderMan()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')


