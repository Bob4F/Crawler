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
import re


def printList(list):
    i = 0
    for item in list:
        i = i + 1
        print("%d:"%i + "%s"%item)

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
# 文档搜索练习

# t_list = bs.find_all("a") # 字符串过滤
# print("查找所有a:")
# print(t_list)



# 正则表达式找内容 search()
# t_list = bs.find_all(re.compile("a"))
# # 展示出所有包含a的内容
# print(t_list)

# t_list = bs.find_all(re.compile("a"))

# def name_is_exist(tag):
#     return tag.has_attr("name")

# t_list = bs.find_all(name_is_exist)

# t_list = bs.find_all(id="head")

# t_list = bs.find_all(class_=True) # 带class属性的内容
# t_list = bs.find_all(href= "//www.baidu.com/duty") # href属性内容匹配
# t_list = bs.find_all(text= "百度首页")

t_list = bs.find_all(text= ["百度首页", "贴吧"])
for item in t_list:
    print(item)

print("-"*30)

# re_list = bs.find_all(text = re.compile("\d"))
re_list = bs.find_all("a", limit=3)
for item in re_list:
    print(item)

print("-"*30)
# 选择器练习

print(bs.select("title"))

class_list = bs.select(".mnav") 
printList(class_list)

print("-"*30)
id_list = bs.select("#u1")
printList(id_list)

print("a_classList"+"-"*30)
a_classList = bs.select("a[class='toindex']")
printList(a_classList)

print("head_metaList"+"-"*30)
var_classList = bs.select("head > meta")
printList(var_classList)

print("unionlist"+"-"*30)
# .toindex的兄弟标签 .toindex
printList(bs.select(".toindex ~ .pf"))
print(bs.select(".toindex ~ .pf")[0].get_text())