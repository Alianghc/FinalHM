#coding:utf-8
import re

import pandas as pd
import numpy as np
import  matplotlib.pyplot
import self as self
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
    plt.bar(range(1, 13), num)
    plt.title('2018 movie release time map')
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
