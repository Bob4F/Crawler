#-*- codeing = utf-8 -*-
#@Author: Fyf


import sqlite3

conn = sqlite3.connect("test.db")
print("Open test.db successful")

sql = '''
    create table test
    (
        id int primary key not null,
        name text not null,
        age int not null,
        addr char(50),
        salary real
    )
'''

conn.execute(sql)

conn.commit()

conn.close()
print("成功建表")





