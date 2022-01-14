#-*- codeing = utf-8 -*-
#Author: Fyf
import fun

dictVar1 = {'key1': 10, 'key2': 20}

print(dictVar1.get("key1"))
print(dictVar1["key2"])
# 异常KeyError: 'key3'
#print(dictVar1["key3"])
# get函数返回None
print(dictVar1.get("key3"))
print(dictVar1.get("key3") == None)

print(dictVar1.get("key3", "default"))

print("-"*30)
print("新增练习")
print(dictVar1.get("id", "default"))
dictVar1["id"] = 1
print(dictVar1.get("id", "default"))

print("-"*30)
print("删除练习")
# 删除了指定键值对，在访问会报错
del dictVar1["id"]
print(dictVar1)

# 删除整个字典
del dictVar1


dictVar2 = {'key1': 10, 'key2': 20}
dictVar2.clear()
print(dictVar2)

# 外部函数调用
fun.f1()