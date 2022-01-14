#-*- codeing = utf-8 -*-
#Author: Fyf

tup1 = ()
print(type(tup1))
tup2 = (1)
print(type(tup2))
tup3 = (1,)
print(type(tup3))


tup4 = (1, 3, "10", "20", "99", "you")
print(tup4[1:])
print(tup4[:3])
print(tup4[1:5])


print("-"*30)

print("元组新增练习")
# 元组对象不支持修改
# tup4[0] = 100

tupVar1 = (12, 24, 36)
tupVar2 = ("abc", "xyz")
tupVar3 = tupVar1 + tupVar2
print(tupVar3)

print("-"*30)
print("元组删除练习")
# 删除变量
del tupVar3
# 空异常 NameError: name 'tupVar3' is not defined
# print(tupVar3)