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
    baseurl = "https://movie.douban.com/top250?start=0"
    # 爬取网页
    datalist = getData(baseurl)
    # 逐一解析数据
    savepath = ".\\豆瓣电影Top250.xls"
    # 保存数据
    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i*25)
        askUrl(url)

    return datalist

def saveData(datalist, savepath):
    print("save....")


def askUrl(baseUrl):
    print("得到一个指定URL的网页内容")
    head = {    
        # 伪装用户代理
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    request = urllib.request.Request(baseUrl, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("uft-8")
        return html
    except Exception as r:
        print("askUrl()发生异常")
        print(r)



if __name__ == "__main__":
    # invoke method 
    main()