# coding:utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data): #收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = file('output.html','w')

        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td width=400 style="word-break:break-all">%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')