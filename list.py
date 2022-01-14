#-*- codeing = utf-8 -*-
#Author: Fyf

nameList = ["小张", "小王", "小李"]

testList = [1, "测试"]


print(testList[0])
print(testList[1])

print(type(testList[0]))
print(type(testList[1]))

'''
print("-----增加前，名单列表的数据----")
for name in nameList :
    print(name)


# nameTemp = input("请输入新学生的名字:")

nameList.append("fyf")

print("-----增加后，名单列表的数据----")
for name in nameList :
    print(name)

var2 = [1, 2]
var3 = [3, 4]
var2.append(var3)

print(var2)
var2.extend(var3)
print(var2)
'''

var4 = [1, 2, 3, 4]

var4.insert(1, 5)
print(var4)


movieName = ["加勒比海盗", "骇客帝国", "指环王", "007", "大内零零发"]

del movieName[2]

print(movieName)

movieName.pop()

print(movieName)

movieName.remove("007")

print(movieName)


print("覆盖指定下标下的元素")
movieName[1] = "骇客帝国2"
print(movieName)


var5 = ["a", "b", "c", "a", "d"]
# 左闭右开
print(var5.index("a", 1, 4))
# 异常 ValueError: 'a' is not in list
# print(var5.index("a", 1, 3))


print("列表里出现了次%d"%var5.count("a"))
