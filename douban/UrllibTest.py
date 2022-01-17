#-*- codeing = utf-8 -*-
#@Author: Fyf

import urllib.request


response = urllib.request.urlopen("http://www.baidu.com")


var1 = open(r"./百度.txt", "w")

var1.write(response.read().decode('utf-8'))


var1.close