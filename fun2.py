#-*- codeing = utf-8 -*-
#Author: Fyf

# 打印一条横线

def printLine(a) :
    for i  in range(a) :
        print("-"*20)


printLine(1)
printLine(10)

# 求三个变量和
def sum(a, b, c):
    return a+b+c


print(sum(1, 5, 4))

# 求平均值
def avg(a, b, c):
    var1 = sum(a,b, c)
    var2 = var1 / 3
    return var2

print(avg(10, 20, 30))

a = 10

def varScope1() :
    a = 100
    print("局部变量%d"%a)


def varScope2():
    print("全局变量%d"%a)


varScope1()
varScope2()
print(a)

