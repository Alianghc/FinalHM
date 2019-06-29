#coding:utf-8
import re

import pandas as pd
import numpy as np
import  matplotlib.pyplot
# import self as self
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# movie
def rank1(movie, name):
    di = {}
    for i in range(0, len(movie)):
        tr = {"title": movie.iloc[i]['title'], "rate": movie.iloc[i]['rate']}
        if tr['rate'] == '':
            continue
        try:
            li = movie.iloc[i][name].split(' / ')
        except AttributeError:
            continue
        for j in li:
            if j not in di.keys():
                di[j] = []
                di[j].append(tr)
            else:
                di[j].append(tr)
    print("----" + name + " rank 3----")
    for key, value in di.items():
        sort = sorted(value, key=lambda x: x['rate'], reverse=True)
        print(key)
        for s in range(3 if len(sort) >= 3 else len(sort)):
            if sort[s]['rate'] != '':
                print(sort[s]['rate'], "  ", sort[s]['title'])
    print("----------END----------")


def rank2(movie, name):
    di = {}
    for i in range(0, len(movie)):
        tr = {"title": movie.iloc[i]['title'], "rate": movie.iloc[i]['rate']}
        if tr['rate'] == '':
            continue
        try:
            li = movie.iloc[i][name].split(',')
        except AttributeError:
            continue
        for j in li:
            if j not in di.keys():
                di[j] = []
                di[j].append(tr)
            else:
                di[j].append(tr)
    print("----" + name + " rank 3----")
    for key, value in di.items():
        sort = sorted(value, key=lambda x: x['rate'], reverse=True)
        print(key)
        for s in range(3 if len(sort) >= 3 else len(sort)):
            if sort[s]['rate'] != '':
                print(sort[s]['rate'], "  ", sort[s]['title'])
    print("----------END----------")

def paint(movie):
    num = [0] * 12
    for i in range(0, len(movie)):
        try:
            for n in re.findall(r"2018-(..)", movie.iloc[i]['date']):
                num[int(n) - 1] += 1
        except TypeError:
            continue
    # x = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
    # width = 0.5
    # idx = np.arange(len(x))
    # plt.bar(idx,num,width,color='green',label='电影柱状图')

    plt.bar(range(1, 13), num, color='green')
    plt.title('2018电影发布时间图')
    plt.xlabel('月份')
    plt.ylabel('电影数量')

    # X = np.arange(12)
    # Y = (1-X/float(12)*np.random.uniform(0.5,1.0,12))
    # for x,y in zip(X,Y):
    #     plt.text(x+0.05,y+0.05,'%.2f' %y, ha='center',va='bottom')


    plt.show()

def main():
    df = pd.read_csv("movie2.csv")
    df.dropna(how='any')
    df1 = df.loc[:,['rate','title']]
    # rank2(df,"type")
    # rank1(df,'region')
    paint(df)


if __name__ == '__main__':
    main()
