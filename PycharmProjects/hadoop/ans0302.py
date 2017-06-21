#!/usr/bin/env python
# coding:utf-8

import pandas as pd
import plt_test as plt

film=pd.read_csv("/home/hadoop/Desktop/arg/arg/film_log3.csv",sep=",",names=['filmname','sdate','edate','company','director','performer','type','turnover','city'])
                                                                            #['电影名称','上映时间','下架时间','制作公司','导演',    '演员',    '类型',    '票房','城市'])
df=film.loc[:,['filmname','sdate','edate','turnover']]
##########################################################################
df['sdate']=pd.to_datetime(df['sdate'],format='%Y-%m-%d')#转化为datetime格式
df['edate']=pd.to_datetime(df['edate'],format='%Y-%m-%d')#转化为datetime格式
################整理电影名称################################################
films=df['filmname'].drop_duplicates().values #获取所有电影名称
################整理票房信息################################################
bors=df['turnover']
borlist=[]
for b in range(0,len(bors)):
    bor=bors[b].replace('票房（万）','')
    borlist.append(float(bor))
df['turnover']=borlist
##########################################################################
def  main(filmname,all=0):
    odf=df[df['filmname']==filmname]
    days=(odf['edate'].max()-odf['sdate'].min()).days+1 #计算该电影的上映的天数
    weeks=days/7+((days%7)>0)                           #计算该电影的上映的周数
    money=odf['turnover'].sum()                         #计算该电影的总票房
    avg = str("%.6f" % (money/weeks))                   #求周平均票房

    if all ==0:
        return [avg]
    else:
        return [filmname,avg]
##########################################################################
datalist1=['《失孤》','《万物生长》','《冲上云霄》']
datlist=[]
for b in datalist1:
    dat=bar(b,0)
    datlist.append(dat[0])
datlist=sorted(datlist,reverse=True)
file2=file('/home/hadoop/Desktop/arg/arg/ans0302.dat','w')
file2.write(datlist[0]+','+datlist[1]+','+datlist[2])
file2.close()
##################################################################################
datalist2=[]
for i in films:
     dat2=bar(i,1)
     datalist2.append(dat2[0]+','+dat2[1]+'\n')
file2=file('/home/hadoop/Desktop/arg/arg/ans0302-1.dat','w')
file2.writelines(datalist2)
file2.close()
##################################################################################
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.hist(df['Age'], bins=7)
# plt.title('Age distribution')
# plt.xlabel('Age')
# plt.ylabel('Employee')
# plt.show()
