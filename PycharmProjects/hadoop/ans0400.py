#!/usr/bin/env python
# coding:utf-8

import pandas as pd
import plt_test as plt

pf=pd.read_table('/home/hadoop/Desktop/arg/arg/arg04/film-csv.txt',sep=';')
del pf['Unnamed: 9']

def score4():

    scr=pd.read_table('/home/hadoop/Desktop/arg/arg/arg04/score.log',sep=',')

    filmnames=scr['film'].drop_duplicates().tolist()
    film_scr={}
    for i in filmnames:
        scrmax =scr[scr['film']==i].groupby('film').max().score.values[0]
        scrmin =scr[scr['film']==i].groupby('film').min().score.values[0]
        scrmedian =scr[scr['film']==i].groupby('film').median().score.values[0]
        scrmean =scr[scr['film']==i].groupby('film').mean().score.values[0]
        film_scr[i]= [str("%.2f"%scrmax),str("%.2f"%scrmin),str("%.2f"%scrmedian),str("%.2f"%scrmean)]
    for k,v in film_scr.items():
        print k.rstrip()+":"+",".join(v)

score4()