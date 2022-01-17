#-*- codeing = utf-8 -*-
#@Author: Fyf

import sys
from bs4 import BeautifulStoneSoup
import re
import urllib.request, urllib.error

import xlwt # 进行excel操作
import sqlite3 # 进行SQLite3数据库操作

def main(): 
    print("hello")
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    # 逐一解析数据
    savepath = ".\\豆瓣电影Top250.xls"
    # 保存数据
    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []
    return datalist


def saveData(datalist, savepath):
    print("save....")


if __name__ == "__main__":
    # invoke method 
    main()