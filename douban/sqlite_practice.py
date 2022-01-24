#-*- codeing = utf-8 -*-
#@Author: Fyf


import re
import sqlite3


# 创建数据表
def createTable(conn) :
    sql = '''
        create table test
        (
            id INTEGER not null primary key autoincrement,
            name text not null,
            age int not null,
            addr char(50),
            salary real
        )
    '''
    conn.execute(sql)
    conn.commit()
    print("成功建表")

def query(cursor):
    sql = "select id,name from test"
    rows = cursor.execute(sql)
    for item in rows:
        print("id = ", item[0])
        print("name = ", item[1])


def insert(conn):
    sql = '''
    insert into test (name, age, addr, salary)
    values ('fyf', 18, 'sz', 1000)
    '''
    conn.execute(sql)
    conn.commit()
    print("成功插入数据")


conn = sqlite3.connect("test.db")
print("Open test.db successful")
# createTable(conn)
# insert(conn)
c = conn.cursor()
query(conn)

conn.close()






