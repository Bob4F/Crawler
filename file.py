#-*- codeing = utf-8 -*-
#@Author: Fyf

import os


path = "test.txt"
file = open(path, "w") # 写模式 打开文件 会覆盖

file.write("hello world\n ttttt")
file.write("2222hello world\n ttttt")
file.write("33333hello world\n ttttt")

file.write("444444hello world\n ttttt")


# 关闭文件
file.close()

file2 = open(path)
# hello
print(file2.read(5))
# worl
print(file2.read(5))
#  文件不存在会报错，如果是以写模式打开，就会新建
# file2 = open("test.txt2")
file2.close



file3 = open(path)
# 读取文件行
print(file3.readlines(1))
print(file3.readlines(1))


file3.close()

print("-"*30)

file4 = open(path)

text = file4.readlines()

# print(text)

i=1
for temp in text:
    print("%d %s"%(i, temp))

file4.close()


os.rename(path, "test-final.txt")

# 删除
# path = "test-final.txt"
# os.remove(path)