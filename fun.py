#-*- codeing = utf-8 -*-
#Author: Fyf

def f1() :
    print("hello world")

# 函数调用
f1()

# 有入参的函数
def addItem(list, item) :
    list.append(item)



list = [1, 2]
addItem(list, 3)
print(list)

# 带返回值的函数
def getSum(a, b) :
    return a+b

print(getSum(1, 10))


# 返回多个值
def divid(a, b) :
    shang = a //b
    yushu = a % b
    return shang, yushu

shang, yu = divid(5, 7)
print("商：%d， 余数：%d"%(shang, yu))