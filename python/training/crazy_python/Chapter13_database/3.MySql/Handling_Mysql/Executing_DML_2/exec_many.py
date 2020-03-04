#与SQLite数据库模块类似的是，MySQL数据库模块同样支持使用executemany()方法重复执行一条SQL语句。

import mysql.connector


#1.连接数据库
conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',port='3306',database='python',use_unicode=True)


#2.获取游标
c = conn.cursor()

#3.调用exectemany()方法多次执行同一条SQL语句
c.executemany('insert into user_tb values(null,%s,%s,%s)',
            (('小红','123456','male'),
             ('小绿','77777','female'),
             ('小蓝','55555','male'),
             ('小紫','13333','female')))

conn.commit()

#4.关闭游标
c.close()

#5.关闭连接
conn.close()


'''
该程序与前面使用的SQLite数据库模块重复执行SQL语句执行的程序基本相同，只是该程序在SQL语句中使用了%s作为占位符.

使用MySQL数据库模块中游标的executemany()方法同样可以重复执行update、delete语句。
'''