# coding:utf-8
import pandas as pd
import numpy as np

##一、创建对象
##1、可以通过传递一个list对象来创建一个Series，pandas会默认创建整型索引：
s=pd.Series([1,3,6,np.nan,44,1])
print s ##float64
print '____________________'
##2、通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame：
dates=pd.date_range('20160101',periods=6)
print dates ##datetime64[ns]
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print df
print '____________________'

