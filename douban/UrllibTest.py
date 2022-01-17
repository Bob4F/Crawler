#-*- codeing = utf-8 -*-
#@Author: Fyf

import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 获取get请求
response = urllib.request.urlopen("http://www.baidu.com")
var1 = open(r"./百度.html", "w")
var1.write(response.read().decode('utf-8'))
var1.close


# post请求
var2 = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding='utf-8')
response2 = urllib.request.urlopen("http://httpbin.org/post", data=var2)
print(response2.read().decode('utf-8'))

print("-"*30)

# 超时处理
try:
    response3 = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response3.read().decode('utf-8'))
except Exception as r:
    print("发生了异常:")
    print(r)

print("-"*30)

# 响应头
response4 = urllib.request.urlopen("http://httpbin.org/get" )
print("请求码:%s"%response4.status)
print("请求头：")
print(response4.getheaders())

print("-"*30)

httpbinUrl = "http://httpbin.org/post"

headObj = {
"User=Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
}

requestData = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding='utf-8')

reqObj = urllib.request.Request(url=httpbinUrl,data=requestData,headers=headObj,method="POST")

try:
    response5 = urllib.request.urlopen(reqObj)
    print(response5.read().decode('utf-8'))
except Exception as r:
    print("访问%s发生异常:"%httpbinUrl)
    print(r)

doubanUrl="https://www.douban.com"
doubanHead = {
"User=Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
}
try:
    doubanReq=urllib.request.Request(url=doubanUrl, headers=doubanHead)
    doubanResp = urllib.request.urlopen(doubanReq)
    print(doubanResp.read().decode('utf-8'))
except Exception as r:
    print("访问%s发生异常:"%doubanUrl)
    print(r)
