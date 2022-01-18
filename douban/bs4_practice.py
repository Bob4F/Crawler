#-*- codeing = utf-8 -*-
#@Author: Fyf

'''
BS4 将复杂html文件转为一个树形结构， 每个节点都是python对象
所有对象归集为4种
1. Tag 标签
2. NavigableString 标签里的字符串内容
3. BeautifulSoup 整个html对象
4. Comment
'''

import bs4

file = open("./百度.html", "rb")
html = file.read()
bs = bs4.BeautifulSoup(html, "html.parser")

print("-"*30)
print(bs.title)
print(type(bs.title.string))

print("-"*30)
print(bs.a)

print(type(bs.a.string))
# print(bs.a.string)

# 获取标签属性
print(bs.a.attrs)


print("-"*30)
# print(bs.head)
print(bs.meta)

print("-"*30)
print(type(bs))
# print(bs)
print(bs.name)
print(bs.attrs)

print("-"*30)
print(bs.head.content)
print(bs.head.children)

print("-"*30)
# 搜索练习

