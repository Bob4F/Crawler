# -*- coding:UTF-8 -*-
#@Author fyf

# for i in range(5):
#     print(i)

for i in range(0, 11, 3):
    print(i)


for i in range(-10, -100, -30):
    print(i)


print("-------------")
cityName = "shenzhen"
for var1 in cityName:
    print(var1, end= "\t")


print("\n-------------")
a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i+1, a[i])

print("-------------")
var2 = 0
while var2<5 :
    print("当前是第%d次执行循环"%(var2+1))
    print("i=%d"%var2)
    var2 += 1

print("求和练习-------------")

sum = 0
for i in range(100):
    sum += i+1

print("求和%d"%sum)

print("while else-------------")
var3 = 0
while var3 < 10 :
    var3 += 3
else :
    print("var3大于等于10：%d"%var3)

print("break ----------")
var4 = 0
while var4 < 10:
    var4 = var4+1
    print("-"*15)
    print(var4)
    if var4 == 5:
        break

print(var4)
