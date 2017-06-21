#!/usr/bin/env python
# coding:utf-8

import pandas as pd

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
def main(filmname,all=0):
    odf=df[df['filmname']==filmname]
    days=(odf['edate'].max()-odf['sdate'].min()).days+1 #计算该电影的上映的天数
    money=odf['turnover'].sum()                         #计算该电影的总票房
    avg = str("%.6f" % (money / days))                  #求日平均票房

    if all ==0:
        return [str(days),avg]
    else:
        return [filmname,str(days), avg]
##########################################################################
data1=main('《冲上云霄》')
file1=file('/home/hadoop/Desktop/arg/arg/ans0301.dat','w')
file1.write(data1[0]+','+data1[1])
file1.close()
##################################################################################
datalist=[]
for i in films:
    dat=main(i,1)
    datalist.append(dat[0]+','+dat[1]+','+dat[2]+'\n')
file2=file('/home/hadoop/Desktop/arg/arg/ans0301-1.dat','w')
file2.writelines(datalist)
file2.close()