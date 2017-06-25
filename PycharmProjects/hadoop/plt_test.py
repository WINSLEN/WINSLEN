#!/usr/bin/env python
# coding:utf-8


import matplotlib.pyplot as plt
import pandas as pd

def plot():
    x = [1,2,3]
    y = [5,7,4]

    x2 = [1,2,3]
    y2 = [10,14,12]

    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')

    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

def bar():
    plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")

    plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')

    plt.title('Epic Graph\nAnother Line! Whoa')

    plt.show()

def hist():

    population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75,
                       65, 54, 44, 43, 42, 48,11,12,12,13,14]

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

    abc=plt.hist(population_ages, bins, histtype='bar', rwidth=0.8,label="Example one" )

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

def bar_chart_generator():
    l = [1,2,3,4,5]
    h = [20, 14, 38, 27, 9]
    w = [0.1, 0.2, 0.3, 0.4, 0.5]
    b = [1,2,3,4,5]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects = ax.bar(l, h, w, b,
                   color='#ffff00',
                   edgecolor='#000000',
                   linewidth=2,
                   #xerr=1,
                   #yerr=2,
                   #ecolor='#999999',
                   #capsize=100,
                   align='center',
                   #orientation='horizontal',
                  )
    #plt.savefig('bar.png')
    plt.show()

def scatter():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plt.scatter(x, y, label='skitscat', color='k', s=20, marker="o")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()



scatter()
