#-*- codeing = utf-8 -*-
#@Author: Fyf

import time


try:
    print("-------------1")
    # 用只读打开了一个不存在的文件
    f=open("123.txt")

    print("-------------2") # 该行代码不会执行
except (IOError, NameError):
    pass



print("-------------3")
var2 = 0
del var2
try:
    print(var2)
except NameError:
    print("变量空指针异常")

print("-------------4")


try:
    # 用只读打开了一个不存在的文件
    f=open("123.txt")
    print("-------------2") # 该行代码不会执行

except (IOError, NameError) as result :
    print("发生了异常")
    print(result)
    pass


print("-------------5")
try:
    # 用只读打开了一个不存在的文件
    f=open("123.txt")
    print("-------------2") # 该行代码不会执行

except Exception as result :
    print("发生了异常")
    print(result)
    pass

# time.sleep(2)






