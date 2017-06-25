#coding=utf-8

from bs4 import BeautifulSoup

html_doc= ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b></p>',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b></p>',
       '</html>']

sout = BeautifulSoup(''.join(html_doc), 'html.parser',from_encoding = 'utf-8')

datas = sout.find_all('b')
for d in datas:
    print d.get_text()



#  if( data="号码" ,vlookup(data,$J$6:$M$6,3,0), vlookup(data,$J$6:$M$6,2,0) )

#  if( vlookup(data,$J$6:$M$6,4,0) = "广州",1,其他)

