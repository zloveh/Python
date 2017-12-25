import urllib.request
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        header = 'User-Agent', 'Mozillaiiik /5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        opener=urllib.request.build_opener()
        opener.handlers=[header]
        r=opener.open(url)
        return r
