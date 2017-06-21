#!/usr/bin/python2.7
# coding:utf-8

import urllib
import re

html=urllib.urlopen("/home/hadoop/Desktop/arg/arg/task0202/movie_review.htm")
text=html.read()
data=re.findall(r'<span class="subject-rate">[0-9].[0-9]</span>',text)
total=[]
for i in data:
    #print i[27:-7]
    score=re.findall(r"[0-9].[0-9]",i)
    total.append(float(score[0]))
print "总评分是",sum(total)
avg=sum(total)/len(total)
avg="%.4f"%avg
print "平均评分是",avg

f=file('/home/hadoop/Desktop/arg/arg/task0202/ans0202.txt',"w")
f.write(str(avg))
f.close()