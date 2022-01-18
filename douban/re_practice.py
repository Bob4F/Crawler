#-*- codeing = utf-8 -*-
#@Author: Fyf

import re

email = "13715166404@163.com"

var1=re.compile(".*@136.com").search(email)
print(var1)
print(re.compile(".*@163.com").search(email))

print(re.search(".*@163.com", email))

print(re.findall("a", "ASDesjaKKeaII"))

print("-"*30)

print(re.findall("[A-B]+", "ASDesjaKKECBeaII"))

print("-"*30)

print(re.sub('a', 'A', "aBcdefGABaaaa"))
