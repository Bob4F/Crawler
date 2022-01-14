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
