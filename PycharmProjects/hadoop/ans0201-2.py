#!/usr/bin/env python
# coding:utf-8

import re
import csv

csvfile = file('/home/hadoop/Desktop/arg/arg/task0201/ans0201(csv包).csv',"w")
writer = csv.writer(csvfile)
file=open('task0201/spider.log','r')
ag=[]

for h in file:
    web="http://www.movie.com/bor/"
    if web in h:
        txt=re.split(";",h)
        for i in txt:
            if re.findall(r'票房',i):
                piaofang=i[15:]
        writer.writerow([txt[0].split(",")[2],txt[1],txt[2],piaofang])

csvfile.close()