#-*- codeing = utf-8 -*-
#@Author: Fyf

import sys
import bs4
import re
import urllib.request, urllib.error
import xlwt # 进行excel操作
import sqlite3 # 进行SQLite3数据库操作
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def main(): 
    baseurl = "https://movie.douban.com/top250?start=0"
    # 爬取网页
    datalist = getData(baseurl)
    # 逐一解析数据
    savepath = "豆瓣电影Top250.xls"
    # 保存数据
    saveData(datalist, savepath)


findLink = re.compile(r'<a href="(.*?)">')
findImg = re.compile(r'<img.*? src="(.*?)">', re.S)
findMovieTitle = re.compile(r'<span class="title">(.*)</span>')
findMovieComment = re.compile(r'<span>(\d*)人评价</span>')

def printMovieLink(item):
        link = re.findall(findLink, str(item))[0]
        print(link)

def printMovieLink(item, data):
    link = re.findall(findLink, str(item))[0]
    print(link)
    data.append(link)

def printMovieTitle(item, data):
    title = re.findall(findMovieTitle, str(item))[0]
    print(title)
    data.append(title)
    try:
        title2 = re.findall(findMovieTitle, str(item))[1]
        solTitle = title2.replace("\xa0", "")
        solTitle2 = solTitle.replace("/", "")
        print(solTitle2)
        data.append(solTitle2)
    except Exception as r:
        print("异常信息：%s"%r)
        data.append('   ')


def printMovieMovieComment(item):
    commentNum = re.findall(findMovieComment, str(item))[0]
    print(commentNum)


findMovieBd = re.compile(r'<div class="bd">(.*)</div>', re.S)
def solBd(item):
    bdList = re.findall(findMovieBd, str(item))
    if len(bdList) > 0:
        print(bdList[0])
    else: 
        print("bd的块不存在")


def getData(baseurl):
    datalist = []
    for i in range(1):
        url = baseurl + str(i*25)
        html = askUrl(url)
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item", limit=3):
            # print(item)
            data =[]
            printMovieLink(item, data)
            printMovieTitle(item, data)
            printMovieMovieComment(item)
            solBd(item)
            print("-"*30)
            datalist.append(data)
    return datalist

def saveData(datalist, savepath):
    print("save....")
    spiderFile = xlwt.Workbook(encoding='utf-8')
    sheet = spiderFile.add_sheet("豆瓣电影top", cell_overwrite_ok=True)
    colNames = ("电影链接", "电影名称", "外国名称")
    for i in range(len(colNames)):
        sheet.write(0, i, colNames[i])
    
    for i in range(len(datalist)):
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i+1, j, data[j])
    spiderFile.save(savepath)



def askUrl(baseUrl):
    head = {    
        # 伪装用户代理
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    request = urllib.request.Request(baseUrl, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = ""
        html = response.read()
        return html
    except Exception as r:
        print("askUrl()发生异常")
        print(r)

if __name__ == "__main__":
    # invoke method 
    main()
    