#!/usr/bin/env python
# coding:utf-8

import pandas as pd
#import matplotlib.pyplot as plt

film=pd.read_csv("/home/hadoop/Desktop/arg/arg/film_log3.csv",sep=",",names=['filmname','sdate','edate','company','director','performer','type','turnover','city'])
                                                                            #['电影名称','上映时间','下架时间','制作公司','导演',    '演员',    '类型',    '票房','城市'])
df=film.loc[:,['filmname','sdate','edate','turnover']]
##########################################################################
df['sdate']=pd.to_datetime(df['sdate'],format='%Y-%m-%d')#转化为datetime格式
df['edate']=pd.to_datetime(df['edate'],format='%Y-%m-%d')#转化为datetime格式
################整理票房信息################################################
bors=df['turnover']
borlist=[]
for b in range(0,len(bors)):
    bor=bors[b].replace('票房（万）','')
    borlist.append(float(bor))
df['turnover']=borlist
##########################################################################
def main(filmname,week):
    odf = df[df['filmname'] == filmname]
    days = (odf['edate'].max() - odf['sdate'].min()).days + 1  # 计算该电影的上映的天数
    money=odf['turnover'].sum()                         #计算该电影的总票房
    avg=money/days                                      #求日平均票房
    weeklist=[0]
    while True:
        days=days-7
        if days>0:
            weeklist.append(7)
        elif days<=0:
            weeklist.append(days+7)
            break
    return weeklist[week]*avg

filmlist=[['《冲上云霄》',1],['《天将雄师》',2],['《坏蛋必须死》',3]]
outputlines=[]
for i in filmlist:
    dataline=main(i[0],i[1])
    dataline=str("%.6f"%dataline)
    outputlines.append(dataline)
file=file('/home/hadoop/Desktop/arg/arg/ans0303.dat','w')
file.write(','.join(outputlines))
file.close()
