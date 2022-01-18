#-*- codeing = utf-8 -*-
#@Author: Fyf

import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


httpbinUrl = "http://httpbin.org/post"
httpbinGetUrl = "http://httpbin.org/get"



# 获取get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# var1 = open(r"./百度.html", "w")
# var1.write(response.read().decode('utf-8'))
# var1.close


# post请求
var2 = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding='utf-8')
response2 = urllib.request.urlopen(httpbinUrl, data=var2)
print(response2.read().decode('utf-8'))

print("-"*30)

# 超时处理
try:
    response3 = urllib.request.urlopen(httpbinUrl, timeout=0.01)
    print(response3.read().decode('utf-8'))
except Exception as r:
    print("发生了异常:")
    print(r)

print("-"*30)

# 响应头
response4 = urllib.request.urlopen(httpbinGetUrl)
print("请求码:%s"%response4.status)
print("请求头：")
print(response4.getheaders())

print("-"*30)

headObj = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "accept": "application/json"
}

requestData = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding='utf-8')

reqObj = urllib.request.Request(url=httpbinUrl, data=requestData, headers=headObj, method="POST")

try:
    response5 = urllib.request.urlopen(reqObj)
    print(response5.read().decode('utf-8'))
except Exception as r:
    print("访问%s发生异常:"%httpbinUrl)
    print(r)

print("-"*30)


doubanUrl="https://movie.douban.com/"
doubanHead = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
"Referer": "https://movie.douban.com/top250",
"Accept": "text/html"
}
try:
    doubanReq=urllib.request.Request(url=doubanUrl, headers=doubanHead)
    doubanResp = urllib.request.urlopen(doubanReq)
    print(doubanResp.read().decode('utf-8'))
except Exception as r:
    print("访问%s发生异常:"%doubanUrl)
    print(r)

print("-"*30)

githubUrl = "https://github.com"
githubHead = {
    "Cookie": "_gh_sess=fkljasfjaljfsajfas",
    "Accept": "text/html",
    "Accept-Encoding": "gzip,deflate,br",
    "accept-language":"zh-CN,zh;q=0.9",
    "sec-ch-ua-platform": "macOS",
    "Host": "192.168.2.72",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
try:
    githubReqObj=urllib.request.Request(url=githubUrl, headers=githubHead)
    githubResp = urllib.request.urlopen(githubReqObj)
    print(githubResp.read().decode('utf-8'))
except Exception as r:
    print("访问%s发生异常:"%githubUrl)
    print(r)
