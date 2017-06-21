#!/usr/bin/env python
# coding:utf-8

import re
import pandas as pd

file=open('/home/hadoop/Desktop/arg/arg/task0201/spider.log','r')
ag=[]
for h in file:
    web="http://www.movie.com/bor/"
    if web in h:
        txt=re.split(";",h)
        for i in txt:
            if re.findall(r'票房',i):
                piaofang=i[15:]
        ag.append([txt[0].split(",")[2],txt[1],txt[2],piaofang])
df = pd.DataFrame(ag,columns=('电影名称','上映日期','结束放映日期','票房（万'))
df = df.drop_duplicates()
df.to_csv('/home/hadoop/Desktop/arg/arg/task0201/ans0201.csv',encoding="utf-8",index=False)

