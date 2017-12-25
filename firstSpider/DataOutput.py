import codecs
class DataOutput(object):
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=codecs.open('C:/Users/账套/Desktop/爬取网页/百度百科.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td width=50px>%s</td>'%data['title'])
            fout.write('<td width=50px></td>')
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('/html')
        fout.close()