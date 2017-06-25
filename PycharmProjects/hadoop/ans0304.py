#!/usr/bin/env python
# coding:utf-8

import pandas as pd
import calendar
import datetime
#import matplotlib.pyplot as plt

film=pd.read_csv("/home/hadoop/Desktop/arg/arg/film_log3.csv",sep=",",names=['filmname','sdate','edate','company','director','performer','type','turnover','city'])
                                                                            #['电影名称','上映时间','下架时间','制作公司','导演',    '演员',    '类型',    '票房','城市'])
df=film.loc[:,['filmname','sdate','edate','turnover','city']]
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
def main(filmname,year,pf):
    odf = pf[pf['filmname'] == filmname]
##########################################################################
    days=(odf['edate'].max()-odf['sdate'].min()).days+1
    boravg=float(odf['turnover'].values/days)                         #求该票房在该城市的日均票房
##########################################################################
    dfmonths=[0]*11
    minday=odf['sdate'].min() #电影上映的日期
    maxday=odf['edate'].max() #电影下映的日期
    fyear=minday.year         #设置电影上映日期的年份为上映日期的年份
    fmonth=minday.month       #设置电影上映日期的月份->当作为循环的初始月份（亦循环的当前月份）
    lmonth=maxday.month       #设置电影下映日期的月份->当作为循环的最终月份
    if (year == minday.year) & (minday.year != maxday.year):      #判断电影是否跨年放映 #判断所求年份是否为上映的年份
        lmonth=13                                       #把最终月份设置为(12月份+1)
    elif (year==maxday.year) & (minday.year!=maxday.year):    #判断电影是否跨年放映 #判断所求年份是否为上映的年份   #判断所求年份是下映的年份
        fmonth=1                                        #把初始月份设置为12月份
    elif (minday.year!=year) & (maxday.year!=year):           #判断该电影是否在所求年份有上映
        return [dfmonths,boravg]                                #若无，则返回全年为0的list
    while True:
        if minday.month == maxday.month:      #判断电影上映日期和下映日期是否在同一个月
            monthdays=maxday.day-minday.day+1
            dfmonths[maxday.month]=monthdays
            break
        else:
            while True:
                if fmonth==minday.month:
                    dfmonths[fmonth] = calendar.monthrange(year, fmonth)[1]-minday.day+1
                    fmonth+=1
                elif fmonth<lmonth:
                    dfmonths[fmonth] = calendar.monthrange(year, fmonth)[1]
                    fmonth+=1
                elif fmonth==lmonth:
                    dfmonths[fmonth] = maxday.day
                    return [dfmonths,boravg]

def total(city,year,month):
    starttime=datetime.datetime(year,min(month),1)
    endtime=datetime.datetime(year,max(month)+1,1)
    pf=df[ (df['city']==city) & (df['sdate'] < endtime) & (df['edate']>=starttime)].drop_duplicates()
    print pf
    pfilms=pf['filmname'].values.tolist()
    for m in month:
        sums=0
        for i in pfilms:
            datalist = main(i, year, pf)
            days = datalist[0]
            boravg = datalist[1]
            sums += days[m] * boravg
        print city + str(year)+"年" + str(m) + "月的总票房为" + str("%.6f" % sums) + "万元"

total('武汉',2016,[1,2,3])
total('长沙',2016,[1,2,3])