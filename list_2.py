#-*- codeing = utf-8 -*-
#Author: Fyf

import random

print("列表排序练习")
var1 = [1, 4, 2, 3]
var1.sort()
print(var1)
var1.sort(reverse=True)
print(var1)

print("-"*20)

print("二维列表练习")
schoolName = [[], [], []]

list1 = [["深圳大学", "暨南大学"], ["北京大学", "清华大学"], ["南科院", "农科院"]]

print(list1[0])
print(list1[0][1])

office = [[], [], []]

names =["A", "B", "C", "D", "E", "F", "G"]
for name in names:
    index = random.randint(0, 2)
    office[index].append(name)

print(office)
print("-"*20)