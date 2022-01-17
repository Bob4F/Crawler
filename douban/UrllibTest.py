#-*- codeing = utf-8 -*-
#@Author: Fyf

import urllib.request

# 获取get请求
response = urllib.request.urlopen("http://www.baidu.com")


var1 = open(r"./百度.html", "w")

var1.write(response.read().decode('utf-8'))
var1.close